# DoBootstrap

DoBootstrap



# DoBootstrap

Hook for manual bootstrapping of the application instead of using `bootstrap` array in @NgModule annotation. This hook is invoked only when the `bootstrap` array is empty or not provided.

## API

```
interface DoBootstrap {
  ngDoBootstrap(appRef: ApplicationRef): void;
}
```

### ngDoBootstrap

`void`

@paramappRef`ApplicationRef`

@returns`void`

## Description

Hook for manual bootstrapping of the application instead of using `bootstrap` array in @NgModule annotation. This hook is invoked only when the `bootstrap` array is empty or not provided.

Reference to the current application is provided as a parameter.

See ["Bootstrapping"](../../guide/ngmodules/bootstrapping).

## Usage Notes

The example below uses [`ApplicationRef.bootstrap()`](applicationref#bootstrap) to render the `AppComponent` on the page.

```
class AppModule implements DoBootstrap {
  ngDoBootstrap(appRef: ApplicationRef) {
    appRef.bootstrap(AppComponent); // Or some other component
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/DoBootstrap>
