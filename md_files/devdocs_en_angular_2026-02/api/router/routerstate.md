# RouterState

RouterState



# RouterState

Represents the state of the router as a tree of activated routes.

[ActivatedRoute](activatedroute)[Getting route information](../../guide/routing/common-router-tasks#getting-route-information)

## API

```
class RouterState extends Tree<ActivatedRoute> {
  constructor(root: TreeNode<ActivatedRoute>, snapshot: RouterStateSnapshot): RouterState;
  override snapshot: RouterStateSnapshot;
  toString(): string;
  override readonly root: T;
}
```

### constructor

`RouterState`

@paramroot`TreeNode<ActivatedRoute>`

@paramsnapshot`RouterStateSnapshot`

The current snapshot of the router state

@returns`RouterState`

### snapshot

`RouterStateSnapshot`

The current snapshot of the router state

### toString

`string`

@returns`string`

### root

`T`

## Usage Notes

Every node in the route tree is an [`ActivatedRoute`](activatedroute) instance that knows about the "consumed" URL segments, the extracted parameters, and the resolved data. Use the [`ActivatedRoute`](activatedroute) properties to traverse the tree from any node.

The following fragment shows how a component gets the root node of the current state to establish its own route tree:

```
@Component({templateUrl:'template.html'})
class MyComponent {
  constructor(router: Router) {
    const state: RouterState = router.routerState;
    const root: ActivatedRoute = state.root;
    const child = root.firstChild;
    const id: Observable<string> = child.params.map(p => p.id);
    //...
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterState>
