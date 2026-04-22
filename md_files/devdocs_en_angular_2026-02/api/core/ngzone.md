# NgZone

NgZone



# NgZone

An injectable service for executing work inside or outside of the Angular zone.

[Resolving zone pollution](https://angular.dev/best-practices/zone-pollution#run-tasks-outside-ngzone)

## API

```
class NgZone {
  constructor(options: { enableLongStackTrace?: boolean | undefined; shouldCoalesceEventChangeDetection?: boolean | undefined; shouldCoalesceRunChangeDetection?: boolean | undefined; }): NgZone;
  readonly hasPendingMacrotasks: boolean;
  readonly hasPendingMicrotasks: boolean;
  readonly isStable: boolean;
  readonly onUnstable: EventEmitter<any>;
  readonly onMicrotaskEmpty: EventEmitter<any>;
  readonly onStable: EventEmitter<any>;
  readonly onError: EventEmitter<any>;
  run<T>(fn: (...args: any[]) => T, applyThis?: any, applyArgs?: any[] | undefined): T;
  runTask<T>(fn: (...args: any[]) => T, applyThis?: any, applyArgs?: any[] | undefined, name?: string | undefined): T;
  runGuarded<T>(fn: (...args: any[]) => T, applyThis?: any, applyArgs?: any[] | undefined): T;
  runOutsideAngular<T>(fn: (...args: any[]) => T): T;
  static isInAngularZone(): boolean;
  static assertInAngularZone(): void;
  static assertNotInAngularZone(): void;
}
```

### constructor

`NgZone`

@paramoptions`{ enableLongStackTrace?: boolean | undefined; shouldCoalesceEventChangeDetection?: boolean | undefined; shouldCoalesceRunChangeDetection?: boolean | undefined; }`

@returns`NgZone`

### hasPendingMacrotasks

`boolean`

### hasPendingMicrotasks

`boolean`

### isStable

`boolean`

Whether there are no outstanding microtasks or macrotasks.

### onUnstable

`EventEmitter<any>`

Notifies when code enters Angular Zone. This gets fired first on VM Turn.

### onMicrotaskEmpty

`EventEmitter<any>`

Notifies when there is no more microtasks enqueued in the current VM Turn. This is a hint for Angular to do change detection, which may enqueue more microtasks. For this reason this event can fire multiple times per VM Turn.

### onStable

`EventEmitter<any>`

Notifies when the last `onMicrotaskEmpty` has run and there are no more microtasks, which implies we are about to relinquish VM turn. This event gets called just once.

### onError

`EventEmitter<any>`

Notifies that an error has been delivered.

### run

`T`

Executes the `fn` function synchronously within the Angular zone and returns value returned by the function.

Running functions via `run` allows you to reenter Angular zone from a task that was executed outside of the Angular zone (typically started via [`runOutsideAngular`](ngzone#runOutsideAngular)).

Any future tasks or microtasks scheduled from within this function will continue executing from within the Angular zone.

If a synchronous error happens it will be rethrown and not reported via `onError`.

@paramfn`(...args: any[]) => T`

@paramapplyThis`any`

@paramapplyArgs`any[] | undefined`

@returns`T`

### runTask

`T`

Executes the `fn` function synchronously within the Angular zone as a task and returns value returned by the function.

Running functions via `runTask` allows you to reenter Angular zone from a task that was executed outside of the Angular zone (typically started via [`runOutsideAngular`](ngzone#runOutsideAngular)).

Any future tasks or microtasks scheduled from within this function will continue executing from within the Angular zone.

If a synchronous error happens it will be rethrown and not reported via `onError`.

@paramfn`(...args: any[]) => T`

@paramapplyThis`any`

@paramapplyArgs`any[] | undefined`

@paramname`string | undefined`

@returns`T`

### runGuarded

`T`

Same as `run`, except that synchronous errors are caught and forwarded via `onError` and not rethrown.

@paramfn`(...args: any[]) => T`

@paramapplyThis`any`

@paramapplyArgs`any[] | undefined`

@returns`T`

### runOutsideAngular

`T`

Executes the `fn` function synchronously in Angular's parent zone and returns value returned by the function.

Running functions via [`runOutsideAngular`](ngzone#runOutsideAngular) allows you to escape Angular's zone and do work that doesn't trigger Angular change-detection or is subject to Angular's error handling.

Any future tasks or microtasks scheduled from within this function will continue executing from outside of the Angular zone.

Use [`run`](ngzone#run) to reenter the Angular zone and do work that updates the application model.

@paramfn`(...args: any[]) => T`

@returns`T`

### isInAngularZone

`boolean`

This method checks whether the method call happens within an Angular Zone instance.

@returns`boolean`

### assertInAngularZone

`void`

Assures that the method is called within the Angular Zone, otherwise throws an error.

@returns`void`

### assertNotInAngularZone

`void`

Assures that the method is called outside of the Angular Zone, otherwise throws an error.

@returns`void`

## Description

An injectable service for executing work inside or outside of the Angular zone.

The most common use of this service is to optimize performance when starting a work consisting of one or more asynchronous tasks that don't require UI updates or error handling to be handled by Angular. Such tasks can be kicked off via [`runOutsideAngular`](ngzone#runOutsideAngular) and if needed, these tasks can reenter the Angular zone via [`run`](ngzone#run).

## Usage Notes

### Example

```
import {Component, NgZone} from '@angular/core';

@Component({
  selector: 'ng-zone-demo',
  template: `
    <h2>Demo: NgZone</h2>

    <p>Progress: {{progress}}%</p>
    @if(progress >= 100) {
       <p>Done processing {{label}} of Angular zone!</p>
    }

    <button (click)="processWithinAngularZone()">Process within Angular zone</button>
    <button (click)="processOutsideOfAngularZone()">Process outside of Angular zone</button>
  `,
})
export class NgZoneDemo {
  progress: number = 0;
  label: string;

  constructor(private _ngZone: NgZone) {}

  // Loop inside the Angular zone
  // so the UI DOES refresh after each setTimeout cycle
  processWithinAngularZone() {
    this.label = 'inside';
    this.progress = 0;
    this._increaseProgress(() => console.log('Inside Done!'));
  }

  // Loop outside of the Angular zone
  // so the UI DOES NOT refresh after each setTimeout cycle
  processOutsideOfAngularZone() {
    this.label = 'outside';
    this.progress = 0;
    this._ngZone.runOutsideAngular(() => {
      this._increaseProgress(() => {
        // reenter the Angular zone and display done
        this._ngZone.run(() => { console.log('Outside Done!'); });
      });
    });
  }

  _increaseProgress(doneCallback: () => void) {
    this.progress += 1;
    console.log(`Current progress: ${this.progress}%`);

    if (this.progress < 100) {
      window.setTimeout(() => this._increaseProgress(doneCallback), 10);
    } else {
      doneCallback();
    }
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/NgZone>
