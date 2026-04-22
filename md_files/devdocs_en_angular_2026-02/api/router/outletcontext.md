# OutletContext

OutletContext



# OutletContext

Store contextual information about a [`RouterOutlet`](routeroutlet)

## API

```
class OutletContext {
  constructor(rootInjector: EnvironmentInjector): OutletContext;
  outlet: RouterOutletContract | null;
  route: ActivatedRoute | null;
  children: ChildrenOutletContexts;
  attachRef: ComponentRef<any> | null;
  readonly injector: EnvironmentInjector;
}
```

### constructor

`OutletContext`

@paramrootInjector`EnvironmentInjector`

@returns`OutletContext`

### outlet

`RouterOutletContract | null`

### route

`ActivatedRoute | null`

### children

`ChildrenOutletContexts`

### attachRef

`ComponentRef<any> | null`

### injector

`EnvironmentInjector`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/OutletContext>
