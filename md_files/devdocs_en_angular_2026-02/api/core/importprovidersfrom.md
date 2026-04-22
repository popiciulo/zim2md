# importProvidersFrom

importProvidersFrom



# importProvidersFrom

Collects providers from all NgModules and standalone components, including transitively imported ones.

## API

```
function importProvidersFrom(
  ...sources: ImportProvidersSource[]
): EnvironmentProviders;
```

### importProvidersFrom

`EnvironmentProviders`

Collects providers from all NgModules and standalone components, including transitively imported ones.

Providers extracted via [`importProvidersFrom`](importprovidersfrom) are only usable in an application injector or another environment injector (such as a route injector). They should not be used in component providers.

More information about standalone components can be found in [this guide](../../guide/components/anatomy-of-components#using-components).

@paramsources`ImportProvidersSource[]`

@returns`EnvironmentProviders`

Usage notes

The results of the [`importProvidersFrom`](importprovidersfrom) call can be used in the `bootstrapApplication` call:

```
await bootstrapApplication(RootComponent, {
  providers: [
    importProvidersFrom(NgModuleOne, NgModuleTwo)
  ]
});
```

You can also use the [`importProvidersFrom`](importprovidersfrom) results in the `providers` field of a route, when a standalone component is used:

```
export const ROUTES: Route[] = [
  {
    path: 'foo',
    providers: [
      importProvidersFrom(NgModuleOne, NgModuleTwo)
    ],
    component: YourStandaloneComponent
  }
];
```

## Description

Collects providers from all NgModules and standalone components, including transitively imported ones.

Providers extracted via [`importProvidersFrom`](importprovidersfrom) are only usable in an application injector or another environment injector (such as a route injector). They should not be used in component providers.

More information about standalone components can be found in [this guide](../../guide/components/anatomy-of-components#using-components).

## Usage Notes

The results of the [`importProvidersFrom`](importprovidersfrom) call can be used in the `bootstrapApplication` call:

```
await bootstrapApplication(RootComponent, {
  providers: [
    importProvidersFrom(NgModuleOne, NgModuleTwo)
  ]
});
```

You can also use the [`importProvidersFrom`](importprovidersfrom) results in the `providers` field of a route, when a standalone component is used:

```
export const ROUTES: Route[] = [
  {
    path: 'foo',
    providers: [
      importProvidersFrom(NgModuleOne, NgModuleTwo)
    ],
    component: YourStandaloneComponent
  }
];
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/importProvidersFrom>
