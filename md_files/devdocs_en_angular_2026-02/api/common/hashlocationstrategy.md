# HashLocationStrategy

HashLocationStrategy



# HashLocationStrategy

A [`LocationStrategy`](locationstrategy) used to configure the [`Location`](location) service to represent its state in the [hash fragment](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) of the browser's URL.

## API

```
class HashLocationStrategy extends LocationStrategy implements OnDestroy {
  constructor(_platformLocation: PlatformLocation, _baseHref?: string | undefined): HashLocationStrategy;
  onPopState(fn: LocationChangeListener): void;
  getBaseHref(): string;
  path(includeHash?: boolean): string;
  prepareExternalUrl(internal: string): string;
  pushState(state: any, title: string, path: string, queryParams: string): void;
  replaceState(state: any, title: string, path: string, queryParams: string): void;
  forward(): void;
  back(): void;
  getState(): unknown;
  historyGo(relativePosition?: number): void;
}
```

### constructor

`HashLocationStrategy`

@param\_platformLocation`PlatformLocation`

@param\_baseHref`string | undefined`

@returns`HashLocationStrategy`

### onPopState

`void`

@paramfn`LocationChangeListener`

@returns`void`

### getBaseHref

`string`

@returns`string`

### path

`string`

@paramincludeHash`boolean`

@returns`string`

### prepareExternalUrl

`string`

@paraminternal`string`

@returns`string`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@parampath`string`

@paramqueryParams`string`

@returns`void`

### replaceState

`void`

@paramstate`any`

@paramtitle`string`

@parampath`string`

@paramqueryParams`string`

@returns`void`

### forward

`void`

@returns`void`

### back

`void`

@returns`void`

### getState

`unknown`

@returns`unknown`

### historyGo

`void`

@paramrelativePosition`number`

@returns`void`

## Description

A [`LocationStrategy`](locationstrategy) used to configure the [`Location`](location) service to represent its state in the [hash fragment](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) of the browser's URL.

For instance, if you call `location.go('/foo')`, the browser's URL will become `example.com#/foo`.

## Usage Notes

### Example

```
import {HashLocationStrategy, Location, LocationStrategy} from '@angular/common';
import {Component} from '@angular/core';

@Component({
  selector: 'hash-location',
  providers: [Location, {provide: LocationStrategy, useClass: HashLocationStrategy}],
  template: `
    <h1>HashLocationStrategy</h1>
    Current URL is: <code>{{ location.path() }}</code
    ><br />
    Normalize: <code>/foo/bar/</code> is: <code>{{ location.normalize('foo/bar') }}</code
    ><br />
  `,
  standalone: false,
})
export class HashLocationComponent {
  location: Location;
  constructor(location: Location) {
    this.location = location;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/HashLocationStrategy>
