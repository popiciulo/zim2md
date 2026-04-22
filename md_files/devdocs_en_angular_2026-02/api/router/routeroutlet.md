# RouterOutlet

RouterOutlet



# RouterOutlet

Acts as a placeholder that Angular dynamically fills based on the current router state.

[RouterLink](routerlink)[Route](route)[Show routes with outlets](../../guide/routing/show-routes-with-outlets)

## API

```
class RouterOutlet implements OnDestroy ,OnInit ,RouterOutletContract {
  @Input() name: string;
  @Output('activate') activateEvents: EventEmitter<any>;
  @Output('deactivate') deactivateEvents: EventEmitter<any>;
  @Output('attach') attachEvents: EventEmitter<unknown>;
  @Output('detach') detachEvents: EventEmitter<unknown>;
  readonly @Input() routerOutletData: InputSignal<unknown>;
  readonly isActivated: boolean;
  readonly component: Object;
  readonly activatedRoute: ActivatedRoute;
  readonly activatedRouteData: Data;
  detach(): ComponentRef<any>;
  attach(ref: ComponentRef<any>, activatedRoute: ActivatedRoute): void;
  deactivate(): void;
  activateWith(activatedRoute: ActivatedRoute, environmentInjector: EnvironmentInjector): void;
}
```

### name

`string`

The name of the outlet

### activateEvents

`EventEmitter<any>`

### deactivateEvents

`EventEmitter<any>`

### attachEvents

`EventEmitter<unknown>`

Emits an attached component instance when the [`RouteReuseStrategy`](routereusestrategy) instructs to re-attach a previously detached subtree.

### detachEvents

`EventEmitter<unknown>`

Emits a detached component instance when the [`RouteReuseStrategy`](routereusestrategy) instructs to detach the subtree.

### routerOutletData

`InputSignal<unknown>`

Data that will be provided to the child injector through the [`ROUTER_OUTLET_DATA`](router_outlet_data) token.

When unset, the value of the token is `undefined` by default.

### isActivated

`boolean`

### component

`Object`

### activatedRoute

`ActivatedRoute`

### activatedRouteData

`Data`

### detach

`ComponentRef<any>`

Called when the [`RouteReuseStrategy`](routereusestrategy) instructs to detach the subtree

@returns`ComponentRef<any>`

### attach

`void`

Called when the [`RouteReuseStrategy`](routereusestrategy) instructs to re-attach a previously detached subtree

@paramref`ComponentRef<any>`

@paramactivatedRoute`ActivatedRoute`

@returns`void`

### deactivate

`void`

@returns`void`

### activateWith

`void`

@paramactivatedRoute`ActivatedRoute`

@paramenvironmentInjector`EnvironmentInjector`

@returns`void`

## Description

Acts as a placeholder that Angular dynamically fills based on the current router state.

Each outlet can have a unique name, determined by the optional `name` attribute. The name cannot be set or changed dynamically. If not set, default value is "primary".

```
<router-outlet></router-outlet>
<router-outlet name='left'></router-outlet>
<router-outlet name='right'></router-outlet>
```

Named outlets can be the targets of secondary routes. The [`Route`](route) object for a secondary route has an `outlet` property to identify the target outlet:

`{path: <base-path>, component: <component>, outlet: <target_outlet_name>}`

Using named outlets and secondary routes, you can target multiple outlets in the same [`RouterLink`](routerlink) directive.

The router keeps track of separate branches in a navigation tree for each named outlet and generates a representation of that tree in the URL. The URL for a secondary route uses the following syntax to specify both the primary and secondary routes at the same time:

`http://base-path/primary-route-path(outlet-name:route-path)`

A router outlet emits an activate event when a new component is instantiated, deactivate event when a component is destroyed. An attached event emits when the [`RouteReuseStrategy`](routereusestrategy) instructs the outlet to reattach the subtree, and the detached event emits when the [`RouteReuseStrategy`](routereusestrategy) instructs the outlet to detach the subtree.

```
<router-outlet
  (activate)='onActivate($event)'
  (deactivate)='onDeactivate($event)'
  (attach)='onAttach($event)'
  (detach)='onDetach($event)'></router-outlet>
```

---

## Exported by

- `RouterModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterOutlet?tab=api>
