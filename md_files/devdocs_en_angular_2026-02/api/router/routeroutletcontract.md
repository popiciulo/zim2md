# RouterOutletContract

RouterOutletContract



# RouterOutletContract

An interface that defines the contract for developing a component outlet for the [`Router`](router).

[ChildrenOutletContexts](childrenoutletcontexts)

## API

```
interface RouterOutletContract {
  isActivated: boolean;
  component: Object | null;
  activatedRouteData: Data;
  activatedRoute: ActivatedRoute | null;
  activateWith(activatedRoute: ActivatedRoute, environmentInjector: EnvironmentInjector): void;
  deactivate(): void;
  detach(): ComponentRef<unknown>;
  attach(ref: ComponentRef<unknown>, activatedRoute: ActivatedRoute): void;
  activateEvents?: EventEmitter<unknown> | undefined;
  deactivateEvents?: EventEmitter<unknown> | undefined;
  attachEvents?: EventEmitter<unknown> | undefined;
  detachEvents?: EventEmitter<unknown> | undefined;
  readonly supportsBindingToComponentInputs?: true | undefined;
}
```

### isActivated

`boolean`

Whether the given outlet is activated.

An outlet is considered "activated" if it has an active component.

### component

`Object | null`

The instance of the activated component or `null` if the outlet is not activated.

### activatedRouteData

`Data`

The [`Data`](data) of the [`ActivatedRoute`](activatedroute) snapshot.

### activatedRoute

`ActivatedRoute | null`

The [`ActivatedRoute`](activatedroute) for the outlet or `null` if the outlet is not activated.

### activateWith

`void`

Called by the [`Router`](router) when the outlet should activate (create a component).

@paramactivatedRoute`ActivatedRoute`

@paramenvironmentInjector`EnvironmentInjector`

@returns`void`

### deactivate

`void`

A request to destroy the currently activated component.

When a [`RouteReuseStrategy`](routereusestrategy) indicates that an [`ActivatedRoute`](activatedroute) should be removed but stored for later re-use rather than destroyed, the [`Router`](router) will call `detach` instead.

@returns`void`

### detach

`ComponentRef<unknown>`

Called when the [`RouteReuseStrategy`](routereusestrategy) instructs to detach the subtree.

This is similar to `deactivate`, but the activated component should *not* be destroyed. Instead, it is returned so that it can be reattached later via the `attach` method.

@returns`ComponentRef<unknown>`

### attach

`void`

Called when the [`RouteReuseStrategy`](routereusestrategy) instructs to re-attach a previously detached subtree.

@paramref`ComponentRef<unknown>`

@paramactivatedRoute`ActivatedRoute`

@returns`void`

### activateEvents

`EventEmitter<unknown> | undefined`

Emits an activate event when a new component is instantiated

### deactivateEvents

`EventEmitter<unknown> | undefined`

Emits a deactivate event when a component is destroyed.

### attachEvents

`EventEmitter<unknown> | undefined`

Emits an attached component instance when the [`RouteReuseStrategy`](routereusestrategy) instructs to re-attach a previously detached subtree.

### detachEvents

`EventEmitter<unknown> | undefined`

Emits a detached component instance when the [`RouteReuseStrategy`](routereusestrategy) instructs to detach the subtree.

### supportsBindingToComponentInputs

`true | undefined`

Used to indicate that the outlet is able to bind data from the [`Router`](router) to the outlet component's inputs.

When this is `undefined` or `false` and the developer has opted in to the feature using [`withComponentInputBinding`](withcomponentinputbinding), a warning will be logged in dev mode if this outlet is used in the application.

## Description

An interface that defines the contract for developing a component outlet for the [`Router`](router).

An outlet acts as a placeholder that Angular dynamically fills based on the current router state.

A router outlet should register itself with the [`Router`](router) via [`ChildrenOutletContexts#onChildOutletCreated`](childrenoutletcontexts#onChildOutletCreated) and unregister with [`ChildrenOutletContexts#onChildOutletDestroyed`](childrenoutletcontexts#onChildOutletDestroyed). When the [`Router`](router) identifies a matched [`Route`](route), it looks for a registered outlet in the [`ChildrenOutletContexts`](childrenoutletcontexts) and activates it.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterOutletContract>
