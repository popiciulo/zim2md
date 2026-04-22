# ChildActivationEnd

ChildActivationEnd



# ChildActivationEnd

An event triggered at the end of the child-activation part of the Resolve phase of routing.

[ChildActivationStart](childactivationstart)[ResolveStart](resolvestart)

## API

```
class ChildActivationEnd {
  constructor(snapshot: ActivatedRouteSnapshot): ChildActivationEnd;
  readonly type: EventType.ChildActivationEnd;
  override snapshot: ActivatedRouteSnapshot;
  toString(): string;
}
```

### constructor

`ChildActivationEnd`

@paramsnapshot`ActivatedRouteSnapshot`

@returns`ChildActivationEnd`

### type

`EventType.ChildActivationEnd`

### snapshot

`ActivatedRouteSnapshot`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ChildActivationEnd>
