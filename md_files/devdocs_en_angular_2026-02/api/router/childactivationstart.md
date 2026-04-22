# ChildActivationStart

ChildActivationStart



# ChildActivationStart

An event triggered at the start of the child-activation part of the Resolve phase of routing.

[ChildActivationEnd](childactivationend)[ResolveStart](resolvestart)

## API

```
class ChildActivationStart {
  constructor(snapshot: ActivatedRouteSnapshot): ChildActivationStart;
  readonly type: EventType.ChildActivationStart;
  override snapshot: ActivatedRouteSnapshot;
  toString(): string;
}
```

### constructor

`ChildActivationStart`

@paramsnapshot`ActivatedRouteSnapshot`

@returns`ChildActivationStart`

### type

`EventType.ChildActivationStart`

### snapshot

`ActivatedRouteSnapshot`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ChildActivationStart>
