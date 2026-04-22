# ROUTER_OUTLET_DATA

ROUTER\_OUTLET\_DATA



# ROUTER\_OUTLET\_DATA

An [`InjectionToken`](../core/injectiontoken) provided by the [`RouterOutlet`](routeroutlet) and can be set using the `routerOutletData` input.

[Page routerOutletData](../../guide/routing/show-routes-with-outlets#passing-contextual-data-to-routed-components)

## API

```
const ROUTER_OUTLET_DATA: InjectionToken<Signal<unknown>>;
```

## Description

An [`InjectionToken`](../core/injectiontoken) provided by the [`RouterOutlet`](routeroutlet) and can be set using the `routerOutletData` input.

When unset, this value is `null` by default.

## Usage Notes

To set the data from the template of the component with `router-outlet`:

```
<router-outlet [routerOutletData]="{name: 'Angular'}" />
```

To read the data in the routed component:

```
data = inject(ROUTER_OUTLET_DATA) as Signal<{name: string}>;
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ROUTER_OUTLET_DATA>
