# ResolveData

ResolveData



# ResolveData

Represents the resolved data associated with a particular route.

[Route#resolve](route#resolve)

## API

```
type ResolveData = {
  [key: string | symbol]: ResolveFn<unknown> | DeprecatedResolve;
}
```

## Description

Represents the resolved data associated with a particular route.

Returning a [`RedirectCommand`](redirectcommand) directs the router to cancel the current navigation and redirect to the location provided in the [`RedirectCommand`](redirectcommand). Note that there are no ordering guarantees when resolvers execute. If multiple resolvers would return a [`RedirectCommand`](redirectcommand), only the first one returned will be used.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ResolveData>
