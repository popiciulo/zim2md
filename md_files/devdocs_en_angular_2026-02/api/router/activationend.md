# ActivationEnd

ActivationEnd



# ActivationEnd

An event triggered at the end of the activation part of the Resolve phase of routing.

[ActivationStart](activationstart)[ResolveStart](resolvestart)

## API

```
class ActivationEnd {
  constructor(snapshot: ActivatedRouteSnapshot): ActivationEnd;
  readonly type: EventType.ActivationEnd;
  override snapshot: ActivatedRouteSnapshot;
  toString(): string;
}
```

### constructor

`ActivationEnd`

@paramsnapshot`ActivatedRouteSnapshot`

@returns`ActivationEnd`

### type

`EventType.ActivationEnd`

### snapshot

`ActivatedRouteSnapshot`

### toString

`string`

@returns`string`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ActivationEnd>
