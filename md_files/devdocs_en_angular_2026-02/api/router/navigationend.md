# NavigationEnd

NavigationEnd



# NavigationEnd

An event triggered when a navigation ends successfully.

[NavigationStart](navigationstart)[NavigationCancel](navigationcancel)[NavigationError](navigationerror)

## API

```
class NavigationEnd extends RouterEvent {
  constructor(id: number, url: string, urlAfterRedirects: string): NavigationEnd;
  readonly type: EventType.NavigationEnd;
  override urlAfterRedirects: string;
  toString(): string;
  override id: number;
  override url: string;
}
```

### constructor

`NavigationEnd`

@paramid`number`

@paramurl`string`

@paramurlAfterRedirects`string`

@returns`NavigationEnd`

### type

`EventType.NavigationEnd`

### urlAfterRedirects

`string`

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
<https://angular.dev/api/router/NavigationEnd>
