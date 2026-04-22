# withDebugTracing

withDebugTracing



# withDebugTracing

Enables logging of all internal navigation events to the console. Extra logging might be useful for debugging purposes to inspect Router event sequence.

[provideRouter](providerouter)

## API

```
function withDebugTracing(): DebugTracingFeature;
```

### withDebugTracing

`DebugTracingFeature`

Enables logging of all internal navigation events to the console. Extra logging might be useful for debugging purposes to inspect Router event sequence.

@returns`DebugTracingFeature`

Usage notes

Basic example of how you can enable debug tracing:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withDebugTracing())
    ]
  }
);
```

## Usage Notes

Basic example of how you can enable debug tracing:

```
const appRoutes: Routes = [];
bootstrapApplication(AppComponent,
  {
    providers: [
      provideRouter(appRoutes, withDebugTracing())
    ]
  }
);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/withDebugTracing>
