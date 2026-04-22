# GuardsCheckEnd

GuardsCheckEnd



# GuardsCheckEnd

An event triggered at the end of the Guard phase of routing.

[GuardsCheckStart](guardscheckstart)

## API

```
class GuardsCheckEnd extends RouterEvent {
  constructor(id: number, url: string, urlAfterRedirects: string, state: RouterStateSnapshot, shouldActivate: boolean): GuardsCheckEnd;
  readonly type: EventType.GuardsCheckEnd;
  override urlAfterRedirects: string;
  override state: RouterStateSnapshot;
  override shouldActivate: boolean;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`GuardsCheckEnd`

@paramid`number`

@paramurl`string`

@paramurlAfterRedirects`string`

@paramstate`RouterStateSnapshot`

@paramshouldActivate`boolean`

@returns`GuardsCheckEnd`

### type

`EventType.GuardsCheckEnd`

### urlAfterRedirects

`string`

### state

`RouterStateSnapshot`

### shouldActivate

`boolean`

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
<https://angular.dev/api/router/GuardsCheckEnd>
