# Router Lifecycle and Events

Router Lifecycle and Events



# Router Lifecycle and Events

  

Angular Router provides a comprehensive set of lifecycle hooks and events that allow you to respond to navigation changes and execute custom logic during the routing process.

## Common router events

The Angular Router emits navigation events that you can subscribe to in order to track the navigation lifecycle. These events are available through the [`Router.events`](../../api/router/router#events) observable. This section covers common routing lifecycle events for navigation and error tracking (in chronological order).

| Events | Description |
| --- | --- |
| [`NavigationStart`](../../api/router/navigationstart) | Occurs when navigation begins and contains the requested URL. |
| [`RoutesRecognized`](../../api/router/routesrecognized) | Occurs after the router determines which route matches the URL and contains the route state information. |
| [`GuardsCheckStart`](../../api/router/guardscheckstart) | Begins the route guard phase. The router evaluates route guards like `canActivate` and `canDeactivate`. |
| [`GuardsCheckEnd`](../../api/router/guardscheckend) | Signals completion of guard evaluation. Contains the result (allowed/denied). |
| [`ResolveStart`](../../api/router/resolvestart) | Begins the data resolution phase. Route resolvers start fetching data. |
| [`ResolveEnd`](../../api/router/resolveend) | Data resolution completes. All required data becomes available. |
| [`NavigationEnd`](../../api/router/navigationend) | Final event when navigation completes successfully. The router updates the URL. |
| [`NavigationSkipped`](../../api/router/navigationskipped) | Occurs when the router skips navigation (e.g., same URL navigation). |

The following are common error events:

| Event | Description |
| --- | --- |
| [`NavigationCancel`](../../api/router/navigationcancel) | Occurs when the router cancels navigation. Often due to a guard returning false. |
| [`NavigationError`](../../api/router/navigationerror) | Occurs when navigation fails. Could be due to invalid routes or resolver errors. |

For a list of all lifecycle events, check out the [complete table of this guide](#all-router-events).

## How to subscribe to router events

When you want to run code during specific navigation lifecycle events, you can do so by subscribing to the `router.events` and checking the instance of the event:

```
// Example of subscribing to router events
import { Component, inject, signal, effect } from '@angular/core';
import { Event, Router, NavigationStart, NavigationEnd } from '@angular/router';

@Component({ ... })
export class RouterEventsComponent {
  private readonly router = inject(Router);

  constructor() {
    // Subscribe to router events and react to events
    this.router.events.pipe(takeUntilDestroyed()).subscribe((event: Event) => {
      if (event instanceof NavigationStart) {
        // Navigation starting
        console.log('Navigation starting:', event.url);
      }
      if (event instanceof NavigationEnd) {
        // Navigation completed
        console.log('Navigation completed:', event.url);
      }
    });
  }
}
```

**NOTE:** The [`Event`](../../api/router/event) type from `@angular/router` is named the same as the regular global [`Event`](../../api/router/event) type, but it is different from the [`RouterEvent`](../../api/router/routerevent) type.

## How to debug routing events

Debugging router navigation issues can be challenging without visibility into the event sequence. Angular provides a built-in debugging feature that logs all router events to the console, helping you understand the navigation flow and identify where issues occur.

When you need to inspect a Router event sequence, you can enable logging for internal navigation events for debugging. You can configure this by passing a configuration option ([`withDebugTracing()`](../../api/router/withdebugtracing)) that enables detailed console logging of all routing events.

```
import { provideRouter, withDebugTracing } from '@angular/router';

const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withDebugTracing())
    ]
  }
);
```

For more information, check out the official docs on [`withDebugTracing`](../../api/router/withdebugtracing).

## Common use cases

Router events enable many practical features in real-world applications. Here are some common patterns that are used with router events.

### Loading indicators

Show loading indicators during navigation:

```
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-loading',
  template: `
    @if (loading()) {
      <div class="loading-spinner">Loading...</div>
    }
  `
})
export class AppComponent {
  private router = inject(Router);

  readonly loading = toSignal(
    this.router.events.pipe(
      map(() => !!this.router.getCurrentNavigation())
    ),
    { initialValue: false }
  );
}
```

### Analytics tracking

Track page views for analytics:

```
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { inject, Injectable, DestroyRef } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AnalyticsService {
  private router = inject(Router);
  private destroyRef = inject(DestroyRef);

  startTracking() {
    this.router.events.pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(event => {
        // Track page views when URL changes
        if (event instanceof NavigationEnd) {
           // Send page view to analytics
          this.analytics.trackPageView(event.url);
        }
      });
  }

  private analytics = {
    trackPageView: (url: string) => {
      console.log('Page view tracked:', url);
    }
  };
}
```

### Error handling

Handle navigation errors gracefully and provide user feedback:

```
import { Component, inject, signal } from '@angular/core';
import { Router, NavigationStart, NavigationError, NavigationCancel, NavigationCancellationCode } from '@angular/router';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

@Component({
  selector: 'app-error-handler',
  template: `
    @if (errorMessage()) {
      <div class="error-banner">
        {{ errorMessage() }}
        <button (click)="dismissError()">Dismiss</button>
      </div>
    }
  `
})
export class ErrorHandlerComponent {
  private router = inject(Router);
  readonly errorMessage = signal('');

  constructor() {
    this.router.events.pipe(takeUntilDestroyed()).subscribe(event => {
      if (event instanceof NavigationStart) {
        this.errorMessage.set('');
      } else if (event instanceof NavigationError) {
        console.error('Navigation error:', event.error);
        this.errorMessage.set('Failed to load page. Please try again.');
      } else if (event instanceof NavigationCancel) {
        console.warn('Navigation cancelled:', event.reason);
        if (event.code === NavigationCancellationCode.GuardRejected) {
          this.errorMessage.set('Access denied. Please check your permissions.');
        }
      }
    });
  }

  dismissError() {
    this.errorMessage.set('');
  }
}
```

## All router events

For reference, here is the complete list of all router events available in Angular. These events are organized by category and listed in the order they typically occur during navigation.

### Navigation events

These events track the core navigation process from start through route recognition, guard checks, and data resolution. They provide visibility into each phase of the navigation lifecycle.

| Event | Description |
| --- | --- |
| [`NavigationStart`](../../api/router/navigationstart) | Occurs when navigation starts |
| [`RouteConfigLoadStart`](../../api/router/routeconfigloadstart) | Occurs before lazy loading a route configuration |
| [`RouteConfigLoadEnd`](../../api/router/routeconfigloadend) | Occurs after a lazy-loaded route configuration loads |
| [`RoutesRecognized`](../../api/router/routesrecognized) | Occurs when the router parses the URL and recognizes the routes |
| [`GuardsCheckStart`](../../api/router/guardscheckstart) | Occurs at the start of the guard phase |
| [`GuardsCheckEnd`](../../api/router/guardscheckend) | Occurs at the end of the guard phase |
| [`ResolveStart`](../../api/router/resolvestart) | Occurs at the start of the resolve phase |
| [`ResolveEnd`](../../api/router/resolveend) | Occurs at the end of the resolve phase |

### Activation events

These events occur during the activation phase when route components are being instantiated and initialized. Activation events fire for each route in the route tree, including parent and child routes.

| Event | Description |
| --- | --- |
| [`ActivationStart`](../../api/router/activationstart) | Occurs at the start of route activation |
| [`ChildActivationStart`](../../api/router/childactivationstart) | Occurs at the start of child route activation |
| [`ActivationEnd`](../../api/router/activationend) | Occurs at the end of route activation |
| [`ChildActivationEnd`](../../api/router/childactivationend) | Occurs at the end of child route activation |

### Navigation completion events

These events represent the final outcome of a navigation attempt. Every navigation will end with exactly one of these events, indicating whether it succeeded, was cancelled, failed, or was skipped.

| Event | Description |
| --- | --- |
| [`NavigationEnd`](../../api/router/navigationend) | Occurs when navigation ends successfully |
| [`NavigationCancel`](../../api/router/navigationcancel) | Occurs when the router cancels navigation |
| [`NavigationError`](../../api/router/navigationerror) | Occurs when navigation fails due to an unexpected error |
| [`NavigationSkipped`](../../api/router/navigationskipped) | Occurs when the router skips navigation (e.g., same URL navigation) |

### Other events

There is one additional event that occurs outside the main navigation lifecycle, but it is still part of the router's event system.

| Event | Description |
| --- | --- |
| [`Scroll`](../../api/router/scroll) | Occurs during scrolling |

## Next steps

Learn more about [route guards](route-guards) and [common router tasks](common-router-tasks).

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/routing/lifecycle-and-events>
