# RouterStateSnapshot

RouterStateSnapshot



# RouterStateSnapshot

Represents the state of the router at a moment in time.

## API

```
class RouterStateSnapshot extends Tree<ActivatedRouteSnapshot> {
  constructor(url: string, root: TreeNode<ActivatedRouteSnapshot>): RouterStateSnapshot;
  override url: string;
  toString(): string;
  override readonly root: T;
}
```

### constructor

`RouterStateSnapshot`

@paramurl`string`

The url from which this snapshot was created

@paramroot`TreeNode<ActivatedRouteSnapshot>`

@returns`RouterStateSnapshot`

### url

`string`

The url from which this snapshot was created

### toString

`string`

@returns`string`

### root

`T`

## Description

Represents the state of the router at a moment in time.

This is a tree of activated route snapshots. Every node in this tree knows about the "consumed" URL segments, the extracted parameters, and the resolved data.

The following example shows how a component is initialized with information from the snapshot of the root node's state at the time of creation.

```
@Component({templateUrl:'template.html'})
class MyComponent {
  constructor(router: Router) {
    const state: RouterState = router.routerState;
    const snapshot: RouterStateSnapshot = state.snapshot;
    const root: ActivatedRouteSnapshot = snapshot.root;
    const child = root.firstChild;
    const id: Observable<string> = child.params.map(p => p.id);
    //...
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterStateSnapshot>
