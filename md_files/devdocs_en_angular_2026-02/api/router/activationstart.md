# ActivationStart

ActivationStart



# ActivationStart

An event triggered at the start of the activation part of the Resolve phase of routing.

[ActivationEnd](activationend)[ResolveStart](resolvestart)

## API

```
class ActivationStart {
  constructor(snapshot: ActivatedRouteSnapshot): ActivationStart;
  readonly type: EventType.ActivationStart;
  override snapshot: ActivatedRouteSnapshot;
  toString(): string;
}
```

### constructor

`ActivationStart`

@paramsnapshot`ActivatedRouteSnapshot`

@returns`ActivationStart`

### type

`EventType.ActivationStart`

### snapshot

`ActivatedRouteSnapshot`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ActivationStart>
