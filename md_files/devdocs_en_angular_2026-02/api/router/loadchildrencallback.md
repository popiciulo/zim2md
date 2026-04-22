# LoadChildrenCallback

LoadChildrenCallback



# LoadChildrenCallback

A function that is called to resolve a collection of lazy-loaded routes. Must be an arrow function of the following form: `() => import('...').then(mod => mod.MODULE)` or `() => import('...').then(mod => mod.ROUTES)`

[Route#loadChildren](route#loadChildren)

## API

```
type LoadChildrenCallback = () =>
  | Type<any>
  | NgModuleFactory<any>
  | Routes
  | Observable<Type<any> | Routes | DefaultExport<Type<any>> | DefaultExport<Routes>>
  | Promise<
      NgModuleFactory<any> | Type<any> | Routes | DefaultExport<Type<any>> | DefaultExport<Routes>
    >
```

## Description

A function that is called to resolve a collection of lazy-loaded routes. Must be an arrow function of the following form: `() => import('...').then(mod => mod.MODULE)` or `() => import('...').then(mod => mod.ROUTES)`

For example:

```
[{
  path: 'lazy',
  loadChildren: () => import('./lazy-route/lazy.module').then(mod => mod.LazyModule),
}];
```

or

```
[{
  path: 'lazy',
  loadChildren: () => import('./lazy-route/lazy.routes').then(mod => mod.ROUTES),
}];
```

If the lazy-loaded routes are exported via a `default` export, the `.then` can be omitted:

```
[{
  path: 'lazy',
  loadChildren: () => import('./lazy-route/lazy.routes'),
}];
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/LoadChildrenCallback>
