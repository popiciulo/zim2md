# withInMemoryScrolling

withInMemoryScrolling



# withInMemoryScrolling

Enables customizable scrolling behavior for router navigations.

[provideRouter](providerouter)[ViewportScroller](../common/viewportscroller)

## API

```
function withInMemoryScrolling(
  options?: InMemoryScrollingOptions,
): InMemoryScrollingFeature;
```

### withInMemoryScrolling

`InMemoryScrollingFeature`

Enables customizable scrolling behavior for router navigations.

@paramoptions`InMemoryScrollingOptions`

Set of configuration parameters to customize scrolling behavior, see [`InMemoryScrollingOptions`](inmemoryscrollingoptions) for additional information.

@returns`InMemoryScrollingFeature`

Usage notes

Basic example of how you can enable scrolling feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withInMemoryScrolling())
    ]
  }
);
```

## Usage Notes

Basic example of how you can enable scrolling feature:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withInMemoryScrolling())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withInMemoryScrolling>
