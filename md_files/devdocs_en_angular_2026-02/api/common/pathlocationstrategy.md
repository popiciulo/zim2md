# PathLocationStrategy

PathLocationStrategy



# PathLocationStrategy

A [`LocationStrategy`](locationstrategy) used to configure the [`Location`](location) service to represent its state in the [path](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) of the browser's URL.

## API

```
class PathLocationStrategy extends LocationStrategy implements OnDestroy {
  constructor(_platformLocation: PlatformLocation, href?: string | undefined): PathLocationStrategy;
  onPopState(fn: LocationChangeListener): void;
  getBaseHref(): string;
  prepareExternalUrl(internal: string): string;
  path(includeHash?: boolean): string;
  pushState(state: any, title: string, url: string, queryParams: string): void;
  replaceState(state: any, title: string, url: string, queryParams: string): void;
  forward(): void;
  back(): void;
  getState(): unknown;
  historyGo(relativePosition?: number): void;
}
```

### constructor

`PathLocationStrategy`

@param\_platformLocation`PlatformLocation`

@paramhref`string | undefined`

@returns`PathLocationStrategy`

### onPopState

`void`

@paramfn`LocationChangeListener`

@returns`void`

### getBaseHref

`string`

@returns`string`

### prepareExternalUrl

`string`

@paraminternal`string`

@returns`string`

### path

`string`

@paramincludeHash`boolean`

@returns`string`

### pushState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

@paramqueryParams`string`

@returns`void`

### replaceState

`void`

@paramstate`any`

@paramtitle`string`

@paramurl`string`

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

A [`LocationStrategy`](locationstrategy) used to configure the [`Location`](location) service to represent its state in the [path](https://en.wikipedia.org/wiki/Uniform_Resource_Locator#Syntax) of the browser's URL.

If you're using [`PathLocationStrategy`](pathlocationstrategy), you may provide a [`APP_BASE_HREF`](app_base_href)or add a `<base href>` element to the document to override the default.

For instance, if you provide an [`APP_BASE_HREF`](app_base_href) of `'/my/app/'` and call `location.go('/foo')`, the browser's URL will become `example.com/my/app/foo`. To ensure all relative URIs resolve correctly, the `<base href>` and/or [`APP_BASE_HREF`](app_base_href) should end with a `/`.

Similarly, if you add `<base href='/my/app/'/>` to the document and call `location.go('/foo')`, the browser's URL will become `example.com/my/app/foo`.

Note that when using [`PathLocationStrategy`](pathlocationstrategy), neither the query nor the fragment in the `<base href>` will be preserved, as outlined by the [RFC](https://tools.ietf.org/html/rfc3986#section-5.2.2).

## Usage Notes

### Example

```
import {Location, LocationStrategy, PathLocationStrategy} from '@angular/common';
import {Component} from '@angular/core';

@Component({
  selector: 'path-location',
  providers: [Location, {provide: LocationStrategy, useClass: PathLocationStrategy}],
  template: `
    <h1>PathLocationStrategy</h1>
    Current URL is: <code>{{ location.path() }}</code
    ><br />
    Normalize: <code>/foo/bar/</code> is: <code>{{ location.normalize('foo/bar') }}</code
    ><br />
  `,
  standalone: false,
})
export class PathLocationComponent {
  location: Location;
  constructor(location: Location) {
    this.location = location;
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/PathLocationStrategy>
