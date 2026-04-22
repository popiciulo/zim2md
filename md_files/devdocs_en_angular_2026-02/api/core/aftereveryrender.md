# afterEveryRender

afterEveryRender



# afterEveryRender

## API

```
function afterEveryRender<E = never, W = never, M = never>(
  spec: {
    earlyRead?: (() => E) | undefined;
    write?: ((...args: [E] extends [never] ? [] : [E]) => W) | undefined;
    mixedReadWrite?:
      | ((
          ...args: [W] extends [never] ? ([E] extends [never] ? [] : [E]) : [W]
        ) => M)
      | undefined;
    read?:
      | ((
          ...args: [M] extends [never]
            ? [W] extends [never]
              ? [E] extends [never]
                ? []
                : [E]
              : [W]
            : [M]
        ) => void)
      | undefined;
  },
  options?: AfterRenderOptions | undefined,
): AfterRenderRef;
function afterEveryRender(
  callback: VoidFunction,
  options?: AfterRenderOptions | undefined,
): AfterRenderRef;
```

```
function afterEveryRender<E = never, W = never, M = never>(spec: { earlyRead?: (() => E) | undefined; write?: ((...args: [E] extends [never] ? [] : [E]) => W) | undefined; mixedReadWrite?: ((...args: [W] extends [never] ? [E] extends [never] ? [] : [E] : [W]) => M) | undefined; read?: ((...args: [M] extends [never] ? [W] extends [never] ? [E] extends [never] ? [] : [E] : [W] : [M]) => void) | undefined; }, options?: AfterRenderOptions | undefined): AfterRenderRef;
```

Register callbacks to be invoked each time the application finishes rendering, during the specified phases. The available phases are:

- `earlyRead` Use this phase to **read** from the DOM before a subsequent `write` callback, for example to perform custom layout that the browser doesn't natively support. Prefer the `read` phase if reading can wait until after the write phase. **Never** write to the DOM in this phase.
- `write` Use this phase to **write** to the DOM. **Never** read from the DOM in this phase.
- `mixedReadWrite` Use this phase to read from and write to the DOM simultaneously. **Never** use this phase if it is possible to divide the work among the other phases instead.
- `read` Use this phase to **read** from the DOM. **Never** write to the DOM in this phase.

You should prefer using the `read` and `write` phases over the `earlyRead` and `mixedReadWrite` phases when possible, to avoid performance degradation.

Note that:

- Callbacks run in the following phase order *after each render*:
  1. `earlyRead`
  2. `write`
  3. `mixedReadWrite`
  4. `read`
- Callbacks in the same phase run in the order they are registered.
- Callbacks run on browser platforms only, they will not run on the server.

The first phase callback to run as part of this spec will receive no parameters. Each subsequent phase callback in this spec will receive the return value of the previously run phase callback as a parameter. This can be used to coordinate work across multiple phases.

Angular is unable to verify or enforce that phases are used correctly, and instead relies on each developer to follow the guidelines documented for each value and carefully choose the appropriate one, refactoring their code if necessary. By doing so, Angular is better able to minimize the performance degradation associated with manual DOM access, ensuring the best experience for the end users of your application or library.

Components are not guaranteed to be [hydrated](../../guide/hydration) before the callback runs. You must use caution when directly reading or writing the DOM and layout.

@paramspec`{ earlyRead?: (() => E) | undefined; write?: ((...args: [E] extends [never] ? [] : [E]) => W) | undefined; mixedReadWrite?: ((...args: [W] extends [never] ? [E] extends [never] ? [] : [E] : [W]) => M) | undefined; read?: ((...args: [M] extends [never] ? [W] extends [never] ? [E] extends [never] ? [] : [E] : [W] : [M]) => void) | undefined; }`

The callback functions to register

@paramoptions`AfterRenderOptions | undefined`

Options to control the behavior of the callback

@returns`AfterRenderRef`

Usage notes

Use [`afterEveryRender`](aftereveryrender) to read or write the DOM after each render.

### Example

```
@Component({
  selector: 'my-cmp',
  template: `<span #content>{{ ... }}</span>`,
})
export class MyComponent {
  @ViewChild('content') contentRef: ElementRef;

  constructor() {
    afterEveryRender({
      read: () => {
        console.log('content height: ' + this.contentRef.nativeElement.scrollHeight);
      }
    });
  }
}
```

```
function afterEveryRender(callback: VoidFunction, options?: AfterRenderOptions | undefined): AfterRenderRef;
```

Register a callback to be invoked each time the application finishes rendering, during the `mixedReadWrite` phase.

You should prefer specifying an explicit phase for the callback instead, or you risk significant performance degradation.

Note that the callback will run

- in the order it was registered
- once per render
- on browser platforms only
- during the `mixedReadWrite` phase

Components are not guaranteed to be [hydrated](../../guide/hydration) before the callback runs. You must use caution when directly reading or writing the DOM and layout.

@paramcallback`VoidFunction`

A callback function to register

@paramoptions`AfterRenderOptions | undefined`

Options to control the behavior of the callback

@returns`AfterRenderRef`

Usage notes

Use [`afterEveryRender`](aftereveryrender) to read or write the DOM after each render.

### Example

```
@Component({
  selector: 'my-cmp',
  template: `<span #content>{{ ... }}</span>`,
})
export class MyComponent {
  @ViewChild('content') contentRef: ElementRef;

  constructor() {
    afterEveryRender({
      read: () => {
        console.log('content height: ' + this.contentRef.nativeElement.scrollHeight);
      }
    });
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/afterEveryRender>
