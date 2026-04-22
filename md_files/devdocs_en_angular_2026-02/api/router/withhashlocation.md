# withHashLocation

withHashLocation



# withHashLocation

Provides the location strategy that uses the URL fragment instead of the history API.

[provideRouter](providerouter)[HashLocationStrategy](../common/hashlocationstrategy)

## API

```
function withHashLocation(): RouterHashLocationFeature;
```

### withHashLocation

`RouterHashLocationFeature`

Provides the location strategy that uses the URL fragment instead of the history API.

@returns`RouterHashLocationFeature`

Usage notes

Basic example of how you can use the hash location option:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withHashLocation())
    ]
  }
);
```

## Usage Notes

Basic example of how you can use the hash location option:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withHashLocation())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withHashLocation>
