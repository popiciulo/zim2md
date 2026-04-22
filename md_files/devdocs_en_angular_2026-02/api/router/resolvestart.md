# ResolveStart

ResolveStart



# ResolveStart

An event triggered at the start of the Resolve phase of routing.

[ResolveEnd](resolveend)

## API

```
class ResolveStart extends RouterEvent {
  constructor(id: number, url: string, urlAfterRedirects: string, state: RouterStateSnapshot): ResolveStart;
  readonly type: EventType.ResolveStart;
  override urlAfterRedirects: string;
  override state: RouterStateSnapshot;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`ResolveStart`

@paramid`number`

@paramurl`string`

@paramurlAfterRedirects`string`

@paramstate`RouterStateSnapshot`

@returns`ResolveStart`

### type

`EventType.ResolveStart`

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

## Description

An event triggered at the start of the Resolve phase of routing.

Runs in the "resolve" phase whether or not there is anything to resolve. In future, may change to only run when there are things to be resolved.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/ResolveStart>
