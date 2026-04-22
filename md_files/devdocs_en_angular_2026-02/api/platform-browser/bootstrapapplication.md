# bootstrapApplication

bootstrapApplication



# bootstrapApplication

Bootstraps an instance of an Angular application and renders a standalone component as the application's root component. More information about standalone components can be found in [this guide](../../guide/components/anatomy-of-components#using-components).

## API

```
function bootstrapApplication(
  rootComponent: Type<unknown>,
  options?: ApplicationConfig | undefined,
  context?: BootstrapContext | undefined,
): Promise<ApplicationRef>;
```

### bootstrapApplication

`Promise<ApplicationRef>`

Bootstraps an instance of an Angular application and renders a standalone component as the application's root component. More information about standalone components can be found in [this guide](../../guide/components/anatomy-of-components#using-components).

@paramrootComponent`Type<unknown>`

A reference to a standalone component that should be rendered.

@paramoptions`ApplicationConfig | undefined`

Extra configuration for the bootstrap operation, see [`ApplicationConfig`](../core/applicationconfig) for additional info.

@paramcontext`BootstrapContext | undefined`

Optional context object that can be used to provide a pre-existing platform injector. This is useful for advanced use-cases, for example, server-side rendering, where the platform is created for each request.

@returns`Promise<ApplicationRef>`

Usage notes

The root component passed into this function *must* be a standalone one (should have the `standalone: true` flag in the `@Component` decorator config).

```
@Component({
  standalone: true,
  template: 'Hello world!'
})
class RootComponent {}

const appRef: ApplicationRef = await bootstrapApplication(RootComponent);
```

You can add the list of providers that should be available in the application injector by specifying the `providers` field in an object passed as the second argument:

```
await bootstrapApplication(RootComponent, {
  providers: [
    {provide: BACKEND_URL, useValue: 'https://yourdomain.com/api'}
  ]
});
```

The `importProvidersFrom` helper method can be used to collect all providers from any existing NgModule (and transitively from all NgModules that it imports):

```
await bootstrapApplication(RootComponent, {
  providers: [
    importProvidersFrom(SomeNgModule)
  ]
});
```

Note: the [`bootstrapApplication`](bootstrapapplication) method doesn't include [Testability](../core/testability) by default. You can add [Testability](../core/testability) by getting the list of necessary providers using [`provideProtractorTestingSupport()`](provideprotractortestingsupport) function and adding them into the `providers` array, for example:

```
import {provideProtractorTestingSupport} from '@angular/platform-browser';

await bootstrapApplication(RootComponent, {providers: [provideProtractorTestingSupport()]});
```

## Usage Notes

The root component passed into this function *must* be a standalone one (should have the `standalone: true` flag in the `@Component` decorator config).

```
@Component({
  standalone: true,
  template: 'Hello world!'
})
class RootComponent {}

const appRef: ApplicationRef = await bootstrapApplication(RootComponent);
```

You can add the list of providers that should be available in the application injector by specifying the `providers` field in an object passed as the second argument:

```
await bootstrapApplication(RootComponent, {
  providers: [
    {provide: BACKEND_URL, useValue: 'https://yourdomain.com/api'}
  ]
});
```

The `importProvidersFrom` helper method can be used to collect all providers from any existing NgModule (and transitively from all NgModules that it imports):

```
await bootstrapApplication(RootComponent, {
  providers: [
    importProvidersFrom(SomeNgModule)
  ]
});
```

Note: the [`bootstrapApplication`](bootstrapapplication) method doesn't include [Testability](../core/testability) by default. You can add [Testability](../core/testability) by getting the list of necessary providers using [`provideProtractorTestingSupport()`](provideprotractortestingsupport) function and adding them into the `providers` array, for example:

```
import {provideProtractorTestingSupport} from '@angular/platform-browser';

await bootstrapApplication(RootComponent, {providers: [provideProtractorTestingSupport()]});
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/platform-browser/bootstrapApplication>
