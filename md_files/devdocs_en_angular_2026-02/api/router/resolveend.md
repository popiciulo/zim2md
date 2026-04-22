# ResolveEnd

ResolveEnd



# ResolveEnd

An event triggered at the end of the Resolve phase of routing.

[ResolveStart](resolvestart)

## API

```
class ResolveEnd extends RouterEvent {
  constructor(id: number, url: string, urlAfterRedirects: string, state: RouterStateSnapshot): ResolveEnd;
  readonly type: EventType.ResolveEnd;
  override urlAfterRedirects: string;
  override state: RouterStateSnapshot;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`ResolveEnd`

@paramid`number`

@paramurl`string`

@paramurlAfterRedirects`string`

@paramstate`RouterStateSnapshot`

@returns`ResolveEnd`

### type

`EventType.ResolveEnd`

### urlAfterRedirects

`string`

### state

`RouterStateSnapshot`

### toString

`string`

@returns`string`

### id

`number`

A unique ID that the router assigns to every router navigation.

### url

`string`

The URL that is the destination for this navigation.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ResolveEnd>
