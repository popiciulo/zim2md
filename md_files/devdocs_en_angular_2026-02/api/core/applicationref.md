# ApplicationRef

ApplicationRef



# ApplicationRef

A reference to an Angular application running on a page.

## API

```
class ApplicationRef {
  readonly destroyed: boolean;
  readonly componentTypes: Type<any>[];
  readonly components: ComponentRef<any>[];
  readonly isStable: Observable<boolean>;
  whenStable(): Promise<void>;
  readonly injector: EnvironmentInjector;
  bootstrap<C>(component: Type<C>, rootSelectorOrNode?: any): ComponentRef<C>;
  bootstrap<C>(componentFactory: ComponentFactory<C>, rootSelectorOrNode?: any): ComponentRef<C>;
  tick(): void;
  attachView(viewRef: ViewRef): void;
  detachView(viewRef: ViewRef): void;
  onDestroy(callback: () => void): VoidFunction;
  destroy(): void;
  readonly viewCount: number;
}
```

### destroyed

`boolean`

Indicates whether this instance was destroyed.

### componentTypes

`Type<any>[]`

Get a list of component types registered to this application. This list is populated even before the component is created.

### components

`ComponentRef<any>[]`

Get a list of components registered to this application.

### isStable

`Observable<boolean>`

Returns an Observable that indicates when the application is stable or unstable.

### whenStable

`Promise<void>`

@returns`Promise<void>`

### injector

`EnvironmentInjector`

The [`EnvironmentInjector`](environmentinjector) used to create this application.

### bootstrap

2 overloads

Bootstrap a component onto the element identified by its selector or, optionally, to a specified element.

@paramcomponent`Type<C>`

@paramrootSelectorOrNode`any`

@returns`ComponentRef<C>`

Usage notes

### Bootstrap process

When bootstrapping a component, Angular mounts it onto a target DOM element and kicks off automatic change detection. The target DOM element can be provided using the `rootSelectorOrNode` argument.

If the target DOM element is not provided, Angular tries to find one on a page using the `selector` of the component that is being bootstrapped (first matched element is used).

### Example

Generally, we define the component to bootstrap in the `bootstrap` array of [`NgModule`](ngmodule), but it requires us to know the component while writing the application code.

Imagine a situation where we have to wait for an API call to decide about the component to bootstrap. We can use the `ngDoBootstrap` hook of the [`NgModule`](ngmodule) and call this method to dynamically bootstrap a component.

```
ngDoBootstrap(appRef: ApplicationRef) {
    this.fetchDataFromApi().then((componentName: string) => {
      if (componentName === 'ComponentOne') {
        appRef.bootstrap(ComponentOne);
      } else {
        appRef.bootstrap(ComponentTwo);
      }
    });
  }
```

Optionally, a component can be mounted onto a DOM element that does not match the selector of the bootstrapped component.

In the following example, we are providing a CSS selector to match the target element.

```
ngDoBootstrap(appRef: ApplicationRef) {
    appRef.bootstrap(ComponentThree, '#root-element');
  }
```

While in this example, we are providing reference to a DOM node.

```
ngDoBootstrap(appRef: ApplicationRef) {
    const element = document.querySelector('#root-element');
    appRef.bootstrap(ComponentFour, element);
  }
```

Bootstrap a component onto the element identified by its selector or, optionally, to a specified element.

@deprecated

Passing Component factories as the `Application.bootstrap` function argument is deprecated. Pass Component Types instead.

@paramcomponentFactory`ComponentFactory<C>`

@paramrootSelectorOrNode`any`

@returns`ComponentRef<C>`

Usage notes

### Bootstrap process

When bootstrapping a component, Angular mounts it onto a target DOM element and kicks off automatic change detection. The target DOM element can be provided using the `rootSelectorOrNode` argument.

If the target DOM element is not provided, Angular tries to find one on a page using the `selector` of the component that is being bootstrapped (first matched element is used).

### Example

Generally, we define the component to bootstrap in the `bootstrap` array of [`NgModule`](ngmodule), but it requires us to know the component while writing the application code.

Imagine a situation where we have to wait for an API call to decide about the component to bootstrap. We can use the `ngDoBootstrap` hook of the [`NgModule`](ngmodule) and call this method to dynamically bootstrap a component.

```
ngDoBootstrap(appRef: ApplicationRef) {
    this.fetchDataFromApi().then((componentName: string) => {
      if (componentName === 'ComponentOne') {
        appRef.bootstrap(ComponentOne);
      } else {
        appRef.bootstrap(ComponentTwo);
      }
    });
  }
```

Optionally, a component can be mounted onto a DOM element that does not match the selector of the bootstrapped component.

In the following example, we are providing a CSS selector to match the target element.

```
ngDoBootstrap(appRef: ApplicationRef) {
    appRef.bootstrap(ComponentThree, '#root-element');
  }
```

While in this example, we are providing reference to a DOM node.

```
ngDoBootstrap(appRef: ApplicationRef) {
    const element = document.querySelector('#root-element');
    appRef.bootstrap(ComponentFour, element);
  }
```

### tick

`void`

Invoke this method to explicitly process change detection and its side-effects.

In development mode, `tick()` also performs a second change detection cycle to ensure that no further changes are detected. If additional changes are picked up during this second cycle, bindings in the app have side-effects that cannot be resolved in a single change detection pass. In this case, Angular throws an error, since an Angular application can only have one change detection pass during which all change detection must complete.

@returns`void`

### attachView

`void`

Attaches a view so that it will be dirty checked. The view will be automatically detached when it is destroyed. This will throw if the view is already attached to a ViewContainer.

@paramviewRef`ViewRef`

@returns`void`

### detachView

`void`

Detaches a view from dirty checking again.

@paramviewRef`ViewRef`

@returns`void`

### onDestroy

`VoidFunction`

Registers a listener to be called when an instance is destroyed.

@paramcallback`() => void`

A callback function to add as a listener.

@returns`VoidFunction`

### destroy

`void`

Destroys an Angular application represented by this [`ApplicationRef`](applicationref). Calling this function will destroy the associated environment injectors as well as all the bootstrapped components with their views.

@returns`void`

### viewCount

`number`

Returns the number of attached views.

## Usage Notes

### isStable examples and caveats

Note two important points about `isStable`, demonstrated in the examples below:

- the application will never be stable if you start any kind of recurrent asynchronous task when the application starts (for example for a polling process, started with a `setInterval`, a `setTimeout` or using RxJS operators like `interval`);
- the `isStable` Observable runs outside of the Angular zone.

Let's imagine that you start a recurrent task (here incrementing a counter, using RxJS `interval`), and at the same time subscribe to `isStable`.

```
constructor(appRef: ApplicationRef) {
  appRef.isStable.pipe(
     filter(stable => stable)
  ).subscribe(() => console.log('App is stable now');
  interval(1000).subscribe(counter => console.log(counter));
}
```

In this example, `isStable` will never emit `true`, and the trace "App is stable now" will never get logged.

If you want to execute something when the app is stable, you have to wait for the application to be stable before starting your polling process.

```
constructor(appRef: ApplicationRef) {
  appRef.isStable.pipe(
    first(stable => stable),
    tap(stable => console.log('App is stable now')),
    switchMap(() => interval(1000))
  ).subscribe(counter => console.log(counter));
}
```

In this example, the trace "App is stable now" will be logged and then the counter starts incrementing every second.

Note also that this Observable runs outside of the Angular zone, which means that the code in the subscription to this Observable will not trigger the change detection.

Let's imagine that instead of logging the counter value, you update a field of your component and display it in its template.

```
constructor(appRef: ApplicationRef) {
  appRef.isStable.pipe(
    first(stable => stable),
    switchMap(() => interval(1000))
  ).subscribe(counter => this.value = counter);
}
```

As the `isStable` Observable runs outside the zone, the `value` field will be updated properly, but the template will not be refreshed!

You'll have to manually trigger the change detection to update the template.

```
constructor(appRef: ApplicationRef, cd: ChangeDetectorRef) {
  appRef.isStable.pipe(
    first(stable => stable),
    switchMap(() => interval(1000))
  ).subscribe(counter => {
    this.value = counter;
    cd.detectChanges();
  });
}
```

Or make the subscription callback run inside the zone.

```
constructor(appRef: ApplicationRef, zone: NgZone) {
  appRef.isStable.pipe(
    first(stable => stable),
    switchMap(() => interval(1000))
  ).subscribe(counter => zone.run(() => this.value = counter));
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/ApplicationRef>
