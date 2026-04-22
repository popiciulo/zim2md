# ChildrenOutletContexts

ChildrenOutletContexts



# ChildrenOutletContexts

Store contextual information about the children (= nested) [`RouterOutlet`](routeroutlet)

## API

```
class ChildrenOutletContexts {
  onChildOutletCreated(childName: string, outlet: RouterOutletContract): void;
  onChildOutletDestroyed(childName: string): void;
  onOutletDeactivated(): Map<string, OutletContext>;
  onOutletReAttached(contexts: Map<string, OutletContext>): void;
  getOrCreateContext(childName: string): OutletContext;
  getContext(childName: string): OutletContext | null;
}
```

### onChildOutletCreated

`void`

Called when a [`RouterOutlet`](routeroutlet) directive is instantiated

@paramchildName`string`

@paramoutlet`RouterOutletContract`

@returns`void`

### onChildOutletDestroyed

`void`

Called when a [`RouterOutlet`](routeroutlet) directive is destroyed. We need to keep the context as the outlet could be destroyed inside a NgIf and might be re-created later.

@paramchildName`string`

@returns`void`

### onOutletDeactivated

`Map<string, OutletContext>`

Called when the corresponding route is deactivated during navigation. Because the component get destroyed, all children outlet are destroyed.

@returns`Map<string, OutletContext>`

### onOutletReAttached

`void`

@paramcontexts`Map<string, OutletContext>`

@returns`void`

### getOrCreateContext

`OutletContext`

@paramchildName`string`

@returns`OutletContext`

### getContext

`OutletContext | null`

@paramchildName`string`

@returns`OutletContext | null`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ChildrenOutletContexts>
