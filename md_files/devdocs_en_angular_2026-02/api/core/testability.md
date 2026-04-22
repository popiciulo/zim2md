# Testability

Testability



# Testability

The Testability service provides testing hooks that can be accessed from the browser.

## API

```
class Testability implements PublicTestability {
  constructor(_ngZone: NgZone, registry: TestabilityRegistry, testabilityGetter: GetTestability): Testability;
  isStable(): boolean;
  whenStable(doneCb: Function, timeout?: number | undefined, updateCb?: Function | undefined): void;
  findProviders(using: any, provider: string, exactMatch: boolean): any[];
}
```

### constructor

`Testability`

@param\_ngZone`NgZone`

@paramregistry`TestabilityRegistry`

@paramtestabilityGetter`GetTestability`

@returns`Testability`

### isStable

`boolean`

Whether an associated application is stable

@returns`boolean`

### whenStable

`void`

Wait for the application to be stable with a timeout. If the timeout is reached before that happens, the callback receives a list of the macro tasks that were pending, otherwise null.

@paramdoneCb`Function`

The callback to invoke when Angular is stable or the timeout expires whichever comes first.

@paramtimeout`number | undefined`

Optional. The maximum time to wait for Angular to become stable. If not specified, whenStable() will wait forever.

@paramupdateCb`Function | undefined`

Optional. If specified, this callback will be invoked whenever the set of pending macrotasks changes. If this callback returns true doneCb will not be invoked and no further updates will be issued.

@returns`void`

### findProviders

`any[]`

Find providers by name

@paramusing`any`

The root element to search from

@paramprovider`string`

The name of binding variable

@paramexactMatch`boolean`

Whether using exactMatch

@returns`any[]`

## Description

The Testability service provides testing hooks that can be accessed from the browser.

Angular applications bootstrapped using an NgModule (via [`@NgModule.bootstrap`](ngmodule#bootstrap) field) will also instantiate Testability by default (in both development and production modes).

For applications bootstrapped using the `bootstrapApplication` function, Testability is not included by default. You can include it into your applications by getting the list of necessary providers using the `provideProtractorTestingSupport()` function and adding them into the `options.providers` array. Example:

```
import {provideProtractorTestingSupport} from '@angular/platform-browser';

await bootstrapApplication(RootComponent, providers: [provideProtractorTestingSupport()]);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/Testability>
