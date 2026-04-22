# Component testing scenarios

Component testing scenarios



# Component testing scenarios

  

This guide explores common component testing use cases.

## Component binding

In the example application, the `BannerComponent` presents static title text in the HTML template.

After a few changes, the `BannerComponent` presents a dynamic title by binding to the component's `title` property like this.

```
@Component({
  selector: 'app-banner',
  template: '<h1>{{title()}}</h1>',
  styles: ['h1 { color: green; font-size: 350%}'],
})
export class BannerComponent {
  title = signal('Test Tour of Heroes');
}
```

As minimal as this is, you decide to add a test to confirm that component actually displays the right content where you think it should.

### Query for the <h1>

You'll write a sequence of tests that inspect the value of the `<h1>` element that wraps the *title* property interpolation binding.

You update the `beforeEach` to find that element with a standard HTML `querySelector` and assign it to the `h1` variable.

```
let component: BannerComponent;
  let fixture: ComponentFixture<BannerComponent>;
  let h1: HTMLElement;

  beforeEach(() => {
    fixture = TestBed.createComponent(BannerComponent);
    component = fixture.componentInstance; // BannerComponent test instance
    h1 = fixture.nativeElement.querySelector('h1');
  });
```

### createComponent() does not bind data

For your first test you'd like to see that the screen displays the default `title`. Your instinct is to write a test that immediately inspects the `<h1>` like this:

```
it('should display original title', () => {
    expect(h1.textContent).toContain(component.title);
  });
```

*That test fails* with the message:

```
expected '' to contain 'Test Tour of Heroes'.
```

Binding happens when Angular performs **change detection**.

In production, change detection kicks in automatically when Angular creates a component or the user enters a keystroke, for example.

The [`TestBed.createComponent`](../../api/core/testing/testbed#createComponent) does not trigger change detection by default; a fact confirmed in the revised test:

```
it('no title in the DOM after createComponent()', () => {
    expect(h1.textContent).toEqual('');
  });
```

### detectChanges()

You can tell the [`TestBed`](../../api/core/testing/testbed) to perform data binding by calling `fixture.detectChanges()`. Only then does the `<h1>` have the expected title.

```
it('should display original title after detectChanges()', () => {
    fixture.detectChanges();
    expect(h1.textContent).toContain(component.title);
  });
```

Delayed change detection is intentional and useful. It gives the tester an opportunity to inspect and change the state of the component *before Angular initiates data binding and calls [lifecycle hooks](../components/lifecycle)*.

Here's another test that changes the component's `title` property *before* calling `fixture.detectChanges()`.

```
it('should display a different test title', () => {
    component.title = 'Test Title';
    fixture.detectChanges();
    expect(h1.textContent).toContain('Test Title');
  });
```

### Automatic change detection

The `BannerComponent` tests frequently call `detectChanges`. Many testers prefer that the Angular test environment run change detection automatically like it does in production.

That's possible by configuring the [`TestBed`](../../api/core/testing/testbed) with the [`ComponentFixtureAutoDetect`](../../api/core/testing/componentfixtureautodetect) provider. First import it from the testing utility library:

```
import {ComponentFixtureAutoDetect} from '@angular/core/testing';
```

Then add it to the `providers` array of the testing module configuration:

```
TestBed.configureTestingModule({
      providers: [{provide: ComponentFixtureAutoDetect, useValue: true}],
    });
```

**HELPFUL:** You can also use the `fixture.autoDetectChanges()` function instead if you only want to enable automatic change detection after making updates to the state of the fixture's component. In addition, automatic change detection is on by default when using [`provideZonelessChangeDetection`](../../api/core/providezonelesschangedetection) and turning it off is not recommended.

Here are three tests that illustrate how automatic change detection works.

```
it('should display original title', () => {
    // Hooray! No `fixture.detectChanges()` needed
    expect(h1.textContent).toContain(comp.title);
  });

  it('should still see original title after comp.title change', async () => {
    const oldTitle = comp.title;
    const newTitle = 'Test Title';
    comp.title.set(newTitle);
    // Displayed title is old because Angular didn't yet run change detection
    expect(h1.textContent).toContain(oldTitle);
    await fixture.whenStable();
    expect(h1.textContent).toContain(newTitle);
  });

  it('should display updated title after detectChanges', () => {
    comp.title.set('Test Title');
    fixture.detectChanges(); // detect changes explicitly
    expect(h1.textContent).toContain(comp.title);
  });
```

The first test shows the benefit of automatic change detection.

The second and third test reveal an important limitation. The Angular testing environment does not run change detection synchronously when updates happen inside the test case that changed the component's `title`. The test must call `await fixture.whenStable` to wait for another round of change detection.

**HELPFUL:** Angular does not know about direct updates to values that are not signals. The easiest way to ensure that change detection will be scheduled is to use signals for values read in the template.

### Change an input value with dispatchEvent()

To simulate user input, find the input element and set its `value` property.

But there is an essential, intermediate step.

Angular doesn't know that you set the input element's `value` property. It won't read that property until you raise the element's [`input`](../../api/core/input) event by calling `dispatchEvent()`.

The following example demonstrates the proper sequence.

```
it('should convert hero name to Title Case', async () => {
      harness.fixture.autoDetectChanges();
      // get the name's input and display elements from the DOM
      const hostElement: HTMLElement = harness.routeNativeElement!;
      const nameInput: HTMLInputElement = hostElement.querySelector('input')!;
      const nameDisplay: HTMLElement = hostElement.querySelector('span')!;

      // simulate user entering a new name into the input box
      nameInput.value = 'quick BROWN  fOx';

      // Dispatch a DOM event so that Angular learns of input value change.
      nameInput.dispatchEvent(new Event('input'));

      // Wait for Angular to update the display binding through the title pipe
      await harness.fixture.whenStable();

      expect(nameDisplay.textContent).toBe('Quick Brown  Fox');
    });
```

## Component with external files

The preceding `BannerComponent` is defined with an *inline template* and *inline css*, specified in the [`@Component.template`](../../api/core/component#template) and [`@Component.styles`](../../api/core/component#styles) properties respectively.

Many components specify *external templates* and *external css* with the [`@Component.templateUrl`](../../api/core/component#templateUrl) and [`@Component.styleUrls`](../../api/core/component#styleUrls) properties respectively, as the following variant of `BannerComponent` does.

```
@Component({
  selector: 'app-banner',
  templateUrl: './banner-external.component.html',
  styleUrls: ['./banner-external.component.css'],
})
```

This syntax tells the Angular compiler to read the external files during component compilation.

That's not a problem when you run the CLI `ng test` command because it *compiles the application before running the tests*.

However, if you run the tests in a **non-CLI environment**, tests of this component might fail. For example, if you run the `BannerComponent` tests in a web coding environment such as [plunker](https://plnkr.co), you'll see a message like this one:

```
Error: This test module uses the component BannerComponent
which is using a "templateUrl" or "styleUrls", but they were never compiled.
Please call "TestBed.compileComponents" before your test.
```

You get this test failure message when the runtime environment compiles the source code *during the tests themselves*.

To correct the problem, call `compileComponents()`.

## Component with a dependency

Components often have service dependencies.

The `WelcomeComponent` displays a welcome message to the logged-in user. It knows who the user is based on a property of the injected `UserService`:

```
import {Component, inject, OnInit, signal} from '@angular/core';
import {UserService} from '../model/user.service';

@Component({
  selector: 'app-welcome',
  template: '<h3 class="welcome"><i>{{welcome()}}</i></h3>',
})
export class WelcomeComponent {
  welcome = signal('');
  private userService = inject(UserService);

  constructor() {
    this.welcome.set(
      this.userService.isLoggedIn() ? 'Welcome, ' + this.userService.user().name : 'Please log in.',
    );
  }
}
```

The `WelcomeComponent` has decision logic that interacts with the service, logic that makes this component worth testing.

### Provide service test doubles

A *component-under-test* doesn't have to be provided with real services.

Injecting the real `UserService` could be difficult. The real service might ask the user for login credentials and attempt to reach an authentication server. These behaviors can be hard to intercept. Be aware that using test doubles makes the test behave differently from production so use them sparingly.

### Get injected services

The tests need access to the `UserService` injected into the `WelcomeComponent`.

Angular has a hierarchical injection system. There can be injectors at multiple levels, from the root injector created by the [`TestBed`](../../api/core/testing/testbed) down through the component tree.

The safest way to get the injected service, the way that ***always works***, is to **get it from the injector of the *component-under-test***. The component injector is a property of the fixture's [`DebugElement`](../../api/core/debugelement).

```
// UserService actually injected into the component
    userService = fixture.debugElement.injector.get(UserService);
```

**HELPFUL:** This is *usually* not necessary. Services are often provided in the root or the TestBed overrides and can be retrieved more easily with [`TestBed.inject()`](../../api/core/testing/testbed#inject) (see below).

### TestBed.inject()

This is easier to remember and less verbose than retrieving a service using the fixture's [`DebugElement`](../../api/core/debugelement).

In this test suite, the *only* provider of `UserService` is the root testing module, so it is safe to call [`TestBed.inject()`](../../api/core/testing/testbed#inject) as follows:

```
// UserService from the root injector
    userService = TestBed.inject(UserService);
```

**HELPFUL:** For a use case in which [`TestBed.inject()`](../../api/core/testing/testbed#inject) does not work, see the [*Override component providers*](#override-component-providers) section that explains when and why you must get the service from the component's injector instead.

### Final setup and tests

Here's the complete `beforeEach()`, using [`TestBed.inject()`](../../api/core/testing/testbed#inject):

```
beforeEach(() => {
    fixture = TestBed.createComponent(WelcomeComponent);
    fixture.autoDetectChanges();
    comp = fixture.componentInstance;

    // UserService actually injected into the component
    userService = fixture.debugElement.injector.get(UserService);
    componentUserService = userService;
    // UserService from the root injector
    userService = TestBed.inject(UserService);

    //  get the "welcome" element by CSS selector (e.g., by class name)
    el = fixture.nativeElement.querySelector('.welcome');
  });
```

And here are some tests:

```
it('should welcome the user', async () => {
    await fixture.whenStable();
    const content = el.textContent;
    expect(content).withContext('"Welcome ..."').toContain('Welcome');
    expect(content).withContext('expected name').toContain('Test User');
  });

  it('should welcome "Bubba"', async () => {
    userService.user.set({name: 'Bubba'}); // welcome message hasn't been shown yet
    await fixture.whenStable();
    expect(el.textContent).toContain('Bubba');
  });

  it('should request login if not logged in', async () => {
    userService.isLoggedIn.set(false); // welcome message hasn't been shown yet
    await fixture.whenStable();
    const content = el.textContent;
    expect(content).withContext('not welcomed').not.toContain('Welcome');
    expect(content)
      .withContext('"log in"')
      .toMatch(/log in/i);
  });
```

The first is a sanity test; it confirms that the `UserService` is called and working.

**HELPFUL:** The withContext function (for example, `'expected name'`) is an optional failure label. If the expectation fails, Jasmine appends this label to the expectation failure message. In a spec with multiple expectations, it can help clarify what went wrong and which expectation failed.

The remaining tests confirm the logic of the component when the service returns different values. The second test validates the effect of changing the user name. The third test checks that the component displays the proper message when there is no logged-in user.

## Component with async service

In this sample, the `AboutComponent` template hosts a `TwainComponent`. The `TwainComponent` displays Mark Twain quotes.

```
template: ` <p class="twain">
      <i>{{ quote | async }}</i>
    </p>
    <button type="button" (click)="getQuote()">Next quote</button>
    @if (errorMessage()) {
      <p class="error">{{ errorMessage() }}</p>
    }`,
```

**HELPFUL:** The value of the component's `quote` property passes through an [`AsyncPipe`](../../api/common/asyncpipe). That means the property returns either a `Promise` or an `Observable`.

In this example, the `TwainComponent.getQuote()` method tells you that the `quote` property returns an `Observable`.

```
getQuote() {
    this.errorMessage.set('');
    this.quote = this.twainService.getQuote().pipe(
      startWith('...'),
      catchError((err: any) => {
        this.errorMessage.set(err.message || err.toString());
        return of('...'); // reset message to placeholder
      }),
    );
```

The `TwainComponent` gets quotes from an injected `TwainService`. The component starts the returned `Observable` with a placeholder value (`'...'`), before the service can return its first quote.

The `catchError` intercepts service errors, prepares an error message, and returns the placeholder value on the success channel.

These are all features you'll want to test.

### Testing with a spy

When testing a component, only the service's public API should matter. In general, tests themselves should not make calls to remote servers. They should emulate such calls. The setup in this `app/twain/twain.component.spec.ts` shows one way to do that:

```
beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TwainService],
    });
    testQuote = 'Test Quote';

    // Create a fake TwainService object with a `getQuote()` spy
    const twainService = TestBed.inject(TwainService);
    // Make the spy return a synchronous Observable with the test data
    getQuoteSpy = spyOn(twainService, 'getQuote').and.returnValue(of(testQuote));

    fixture = TestBed.createComponent(TwainComponent);
    fixture.autoDetectChanges();
    component = fixture.componentInstance;
    quoteEl = fixture.nativeElement.querySelector('.twain');
  });
```

Focus on the spy.

```
// Create a fake TwainService object with a `getQuote()` spy
    const twainService = TestBed.inject(TwainService);
    // Make the spy return a synchronous Observable with the test data
    getQuoteSpy = spyOn(twainService, 'getQuote').and.returnValue(of(testQuote));
```

The spy is designed such that any call to `getQuote` receives an observable with a test quote. Unlike the real `getQuote()` method, this spy bypasses the server and returns a synchronous observable whose value is available immediately.

You can write many useful tests with this spy, even though its `Observable` is synchronous.

**HELPFUL:** It is best to limit the usage of spies to only what is necessary for the test. Creating mocks or spies for more than what's necessary can be brittle. As the component and injectable evolves, the unrelated tests can fail because they no longer mock enough behaviors that would otherwise not affect the test.

### Async test with fakeAsync()

To use [`fakeAsync()`](../../api/core/testing/fakeasync) functionality, you must import `zone.js/testing` in your test setup file. If you created your project with the Angular CLI, `zone-testing` is already imported in `src/test.ts`.

The following test confirms the expected behavior when the service returns an `ErrorObservable`.

```
it('should display error when TwainService fails', fakeAsync(() => {
      // tell spy to return an error observable after a timeout
      getQuoteSpy.and.returnValue(
        defer(() => {
          return new Promise((resolve, reject) => {
            setTimeout(() => {
              reject('TwainService test failure');
            });
          });
        }),
      );
      fixture.detectChanges(); // onInit()
      // sync spy errors immediately after init

      tick(); // flush the setTimeout()

      fixture.detectChanges(); // update errorMessage within setTimeout()

      expect(errorMessage())
        .withContext('should display error')
        .toMatch(/test failure/);
      expect(quoteEl.textContent).withContext('should show placeholder').toBe('...');
    }));
```

**HELPFUL:** The `it()` function receives an argument of the following form.

```
fakeAsync(() => { /_test body_/ })
```

The [`fakeAsync()`](../../api/core/testing/fakeasync) function enables a linear coding style by running the test body in a special `fakeAsync test zone`. The test body appears to be synchronous. There is no nested syntax (like a `Promise.then()`) to disrupt the flow of control.

**HELPFUL:** Limitation: The [`fakeAsync()`](../../api/core/testing/fakeasync) function won't work if the test body makes an `XMLHttpRequest` (XHR) call. XHR calls within a test are rare, but if you need to call XHR, use [`waitForAsync()`](../../api/core/testing/waitforasync).

**IMPORTANT:** Be aware that asynchronous tasks that happen inside the [`fakeAsync`](../../api/core/testing/fakeasync) zone need to be manually executed with [`flush`](../../api/core/testing/flush) or [`tick`](../../api/core/testing/tick). If you attempt to wait for them to complete (i.e. using `fixture.whenStable`) without using the [`fakeAsync`](../../api/core/testing/fakeasync) test helpers to advance time, your test will likely fail. See below for more information.

### The tick() function

You do have to call [tick()](../../api/core/testing/tick) to advance the virtual clock.

Calling [tick()](../../api/core/testing/tick) simulates the passage of time until all pending asynchronous activities finish. In this case, it waits for the observable's `setTimeout()`.

The [tick()](../../api/core/testing/tick) function accepts `millis` and `tickOptions` as parameters. The `millis` parameter specifies how much the virtual clock advances and defaults to `0` if not provided. For example, if you have a `setTimeout(fn, 100)` in a [`fakeAsync()`](../../api/core/testing/fakeasync) test, you need to use `tick(100)` to trigger the fn callback. The optional `tickOptions` parameter has a property named `processNewMacroTasksSynchronously`. The `processNewMacroTasksSynchronously` property represents whether to invoke new generated macro tasks when ticking and defaults to `true`.

```
it('should run timeout callback with delay after call tick with millis', fakeAsync(() => {
      let called = false;
      setTimeout(() => {
        called = true;
      }, 100);
      tick(100);
      expect(called).toBe(true);
    }));
```

The [tick()](../../api/core/testing/tick) function is one of the Angular testing utilities that you import with [`TestBed`](../../api/core/testing/testbed). It's a companion to [`fakeAsync()`](../../api/core/testing/fakeasync) and you can only call it within a [`fakeAsync()`](../../api/core/testing/fakeasync) body.

### tickOptions

In this example, you have a new macro task, the nested `setTimeout` function. By default, when the [`tick`](../../api/core/testing/tick) is setTimeout, `outside` and `nested` will both be triggered.

```
it('should run new macro task callback with delay after call tick with millis', fakeAsync(() => {
      function nestedTimer(cb: () => any): void {
        setTimeout(() => setTimeout(() => cb()));
      }
      const callback = jasmine.createSpy('callback');
      nestedTimer(callback);
      expect(callback).not.toHaveBeenCalled();
      tick(0);
      // the nested timeout will also be triggered
      expect(callback).toHaveBeenCalled();
    }));
```

In some case, you don't want to trigger the new macro task when ticking. You can use `tick(millis, {processNewMacroTasksSynchronously: false})` to not invoke a new macro task.

```
it('should not run new macro task callback with delay after call tick with millis', fakeAsync(() => {
      function nestedTimer(cb: () => any): void {
        setTimeout(() => setTimeout(() => cb()));
      }
      const callback = jasmine.createSpy('callback');
      nestedTimer(callback);
      expect(callback).not.toHaveBeenCalled();
      tick(0, {processNewMacroTasksSynchronously: false});
      // the nested timeout will not be triggered
      expect(callback).not.toHaveBeenCalled();
      tick(0);
      expect(callback).toHaveBeenCalled();
    }));
```

### Comparing dates inside fakeAsync()

[`fakeAsync()`](../../api/core/testing/fakeasync) simulates passage of time, which lets you calculate the difference between dates inside [`fakeAsync()`](../../api/core/testing/fakeasync).

```
it('should get Date diff correctly in fakeAsync', fakeAsync(() => {
      const start = Date.now();
      tick(100);
      const end = Date.now();
      expect(end - start).toBe(100);
    }));
```

### jasmine.clock with fakeAsync()

Jasmine also provides a `clock` feature to mock dates. Angular automatically runs tests that are run after `jasmine.clock().install()` is called inside a [`fakeAsync()`](../../api/core/testing/fakeasync) method until `jasmine.clock().uninstall()` is called. [`fakeAsync()`](../../api/core/testing/fakeasync) is not needed and throws an error if nested.

By default, this feature is disabled. To enable it, set a global flag before importing `zone-testing`.

If you use the Angular CLI, configure this flag in `src/test.ts`.

```
[window as any]('__zone_symbol__fakeAsyncPatchLock') = true;
import 'zone.js/testing';
```

```
describe('use jasmine.clock()', () => {
    // need to config __zone_symbol__fakeAsyncPatchLock flag
    // before loading zone.js/testing
    beforeEach(() => {
      jasmine.clock().install();
    });
    afterEach(() => {
      jasmine.clock().uninstall();
    });
    it('should auto enter fakeAsync', () => {
      // is in fakeAsync now, don't need to call fakeAsync(testFn)
      let called = false;
      setTimeout(() => {
        called = true;
      }, 100);
      jasmine.clock().tick(100);
      expect(called).toBe(true);
    });
  });
```

### Using the RxJS scheduler inside fakeAsync()

You can also use RxJS scheduler in [`fakeAsync()`](../../api/core/testing/fakeasync) just like using `setTimeout()` or `setInterval()`, but you need to import `zone.js/plugins/zone-patch-rxjs-fake-async` to patch RxJS scheduler.

```
it('should get Date diff correctly in fakeAsync with rxjs scheduler', fakeAsync(() => {
      // need to add `import 'zone.js/plugins/zone-patch-rxjs-fake-async'
      // to patch rxjs scheduler
      let result = '';
      of('hello')
        .pipe(delay(1000))
        .subscribe((v) => {
          result = v;
        });
      expect(result).toBe('');
      tick(1000);
      expect(result).toBe('hello');

      const start = new Date().getTime();
      let dateDiff = 0;
      interval(1000)
        .pipe(take(2))
        .subscribe(() => (dateDiff = new Date().getTime() - start));

      tick(1000);
      expect(dateDiff).toBe(1000);
      tick(1000);
      expect(dateDiff).toBe(2000);
    }));
```

### Support more macroTasks

By default, [`fakeAsync()`](../../api/core/testing/fakeasync) supports the following macro tasks.

- `setTimeout`
- `setInterval`
- `requestAnimationFrame`
- `webkitRequestAnimationFrame`
- `mozRequestAnimationFrame`

If you run other macro tasks such as `HTMLCanvasElement.toBlob()`, an *"Unknown macroTask scheduled in fake async test"* error is thrown.

```
import {fakeAsync, TestBed, tick} from '@angular/core/testing';

import {CanvasComponent} from './canvas.component';

describe('CanvasComponent', () => {
  it('should be able to generate blob data from canvas', fakeAsync(() => {
    const fixture = TestBed.createComponent(CanvasComponent);
    const canvasComp = fixture.componentInstance;

    fixture.detectChanges();
    expect(canvasComp.blobSize).toBe(0);

    tick();
    expect(canvasComp.blobSize).toBeGreaterThan(0);
  }));
});
```

```
import {Component, AfterViewInit, ViewChild, ElementRef} from '@angular/core';

@Component({
  selector: 'sample-canvas',
  template: '<canvas #sampleCanvas width="200" height="200"></canvas>',
})
export class CanvasComponent implements AfterViewInit {
  blobSize = 0;
  @ViewChild('sampleCanvas') sampleCanvas!: ElementRef;

  ngAfterViewInit() {
    const canvas: HTMLCanvasElement = this.sampleCanvas.nativeElement;
    const context = canvas.getContext('2d')!;

    context.clearRect(0, 0, 200, 200);
    context.fillStyle = '#FF1122';
    context.fillRect(0, 0, 200, 200);

    canvas.toBlob((blob) => {
      this.blobSize = blob?.size ?? 0;
    });
  }
}
```

If you want to support such a case, you need to define the macro task you want to support in `beforeEach()`. For example:

```
beforeEach(() => {
    (window as any).__zone_symbol__FakeAsyncTestMacroTask = [
      {
        source: 'HTMLCanvasElement.toBlob',
        callbackArgs: [{size: 200}],
      },
    ];
  });
```

**HELPFUL:** In order to make the `<canvas>` element Zone.js-aware in your app, you need to import the `zone-patch-canvas` patch (either in `polyfills.ts` or in the specific file that uses `<canvas>`):

```
// Import patch to make async `HTMLCanvasElement` methods (such as `.toBlob()`) Zone.js-aware.
// Either import in `polyfills.ts` (if used in more than one places in the app) or in the component
// file using `HTMLCanvasElement` (if it is only used in a single file).
import 'zone.js/plugins/zone-patch-canvas';
```

### Async observables

You might be satisfied with the test coverage of these tests.

However, you might be troubled by the fact that the real service doesn't quite behave this way. The real service sends requests to a remote server. A server takes time to respond and the response certainly won't be available immediately as in the previous two tests.

Your tests will reflect the real world more faithfully if you return an *asynchronous* observable from the `getQuote()` spy like this.

```
// Simulate delayed observable values with the `asyncData()` helper
      getQuoteSpy.and.returnValue(asyncData(testQuote));
```

### Async observable helpers

The async observable was produced by an `asyncData` helper. The `asyncData` helper is a utility function that you'll have to write yourself, or copy this one from the sample code.

```
/**
 * Create async observable that emits-once and completes
 * after a JS engine turn
 */
export function asyncData<T>(data: T) {
  return defer(() => Promise.resolve(data));
}
```

This helper's observable emits the `data` value in the next turn of the JavaScript engine.

The [RxJS `defer()` operator](http://reactivex.io/documentation/operators/defer.html) returns an observable. It takes a factory function that returns either a promise or an observable. When something subscribes to *defer*'s observable, it adds the subscriber to a new observable created with that factory.

The `defer()` operator transforms the `Promise.resolve()` into a new observable that, like [`HttpClient`](../../api/common/http/httpclient), emits once and completes. Subscribers are unsubscribed after they receive the data value.

There's a similar helper for producing an async error.

```
/**
 * Create async observable error that errors
 * after a JS engine turn
 */
export function asyncError<T>(errorObject: any) {
  return defer(() => Promise.reject(errorObject));
}
```

### More async tests

Now that the `getQuote()` spy is returning async observables, most of your tests will have to be async as well.

Here's a [`fakeAsync()`](../../api/core/testing/fakeasync) test that demonstrates the data flow you'd expect in the real world.

```
it('should show quote after getQuote (fakeAsync)', fakeAsync(() => {
      fixture.detectChanges(); // ngOnInit()
      expect(quoteEl.textContent).withContext('should show placeholder').toBe('...');

      tick(); // flush the observable to get the quote
      fixture.detectChanges(); // update view

      expect(quoteEl.textContent).withContext('should show quote').toBe(testQuote);
      expect(errorMessage()).withContext('should not show error').toBeNull();
    }));
```

Notice that the quote element displays the placeholder value (`'...'`) after `ngOnInit()`. The first quote hasn't arrived yet.

To flush the first quote from the observable, you call [tick()](../../api/core/testing/tick). Then call `detectChanges()` to tell Angular to update the screen.

Then you can assert that the quote element displays the expected text.

### Async test without fakeAsync()

Here's the previous [`fakeAsync()`](../../api/core/testing/fakeasync) test, re-written with the `async`.

```
it('should show quote after getQuote (async)', async () => {
      fixture.detectChanges(); // ngOnInit()
      expect(quoteEl.textContent).withContext('should show placeholder').toBe('...');

      await fixture.whenStable();
      // wait for async getQuote
      fixture.detectChanges(); // update view with quote
      expect(quoteEl.textContent).toBe(testQuote);
      expect(errorMessage()).withContext('should not show error').toBeNull();
    });
```

### whenStable

The test must wait for the `getQuote()` observable to emit the next quote. Instead of calling [tick()](../../api/core/testing/tick), it calls `fixture.whenStable()`.

The `fixture.whenStable()` returns a promise that resolves when the JavaScript engine's task queue becomes empty. In this example, the task queue becomes empty when the observable emits the first quote.

## Component with inputs and outputs

A component with inputs and outputs typically appears inside the view template of a host component. The host uses a property binding to set the input property and an event binding to listen to events raised by the output property.

The testing goal is to verify that such bindings work as expected. The tests should set input values and listen for output events.

The `DashboardHeroComponent` is a tiny example of a component in this role. It displays an individual hero provided by the `DashboardComponent`. Clicking that hero tells the `DashboardComponent` that the user has selected the hero.

The `DashboardHeroComponent` is embedded in the `DashboardComponent` template like this:

```
@for (hero of heroes; track hero) {
    <dashboard-hero
      class="col-1-4"
      [hero]="hero"
      (selected)="gotoDetail($event)"
    >
    </dashboard-hero>
  }
```

The `DashboardHeroComponent` appears in an `@for` block, which sets each component's `hero` input property to the looping value and listens for the component's `selected` event.

Here's the component's full definition:

```
@Component({
  selector: 'dashboard-hero',
  template: `
    <button type="button" (click)="click()" class="hero">
      {{ hero().name | uppercase }}
    </button>
  `,
  styleUrls: ['./dashboard-hero.component.css'],
  imports: [UpperCasePipe],
})
export class DashboardHeroComponent {
  readonly hero = input.required<Hero>();
  readonly selected = output<Hero>();
  click() {
    this.selected.emit(this.hero());
  }
}
```

While testing a component this simple has little intrinsic value, it's worth knowing how. Use one of these approaches:

- Test it as used by `DashboardComponent`
- Test it as a standalone component
- Test it as used by a substitute for `DashboardComponent`

The immediate goal is to test the `DashboardHeroComponent`, not the `DashboardComponent`, so, try the second and third options.

### Test DashboardHeroComponent standalone

Here's the meat of the spec file setup.

```
TestBed.configureTestingModule({
      providers: appProviders,
    });
    fixture = TestBed.createComponent(DashboardHeroComponent);
    fixture.autoDetectChanges();
    comp = fixture.componentInstance;

    // find the hero's DebugElement and element
    heroDe = fixture.debugElement.query(By.css('.hero'));
    heroEl = heroDe.nativeElement;

    // mock the hero supplied by the parent component
    expectedHero = {id: 42, name: 'Test Name'};

    // simulate the parent setting the input property with that hero
    fixture.componentRef.setInput('hero', expectedHero);

    // wait for initial data binding
    await fixture.whenStable();
```

Notice how the setup code assigns a test hero (`expectedHero`) to the component's `hero` property, emulating the way the `DashboardComponent` would set it using the property binding in its repeater.

The following test verifies that the hero name is propagated to the template using a binding.

```
it('should display hero name in uppercase', () => {
    const expectedPipedName = expectedHero.name.toUpperCase();
    expect(heroEl.textContent).toContain(expectedPipedName);
  });
```

Because the template passes the hero name through the Angular [`UpperCasePipe`](../../api/common/uppercasepipe), the test must match the element value with the upper-cased name.

### Clicking

Clicking the hero should raise a `selected` event that the host component (`DashboardComponent` presumably) can hear:

```
it('should raise selected event when clicked (triggerEventHandler)', () => {
    let selectedHero: Hero | undefined;
    comp.selected.subscribe((hero: Hero) => (selectedHero = hero));

    heroDe.triggerEventHandler('click');
    expect(selectedHero).toBe(expectedHero);
  });
```

The component's `selected` property returns an [`EventEmitter`](../../api/core/eventemitter), which looks like an RxJS synchronous `Observable` to consumers. The test subscribes to it *explicitly* just as the host component does *implicitly*.

If the component behaves as expected, clicking the hero's element should tell the component's `selected` property to emit the `hero` object.

The test detects that event through its subscription to `selected`.

### triggerEventHandler

The `heroDe` in the previous test is a [`DebugElement`](../../api/core/debugelement) that represents the hero `<div>`.

It has Angular properties and methods that abstract interaction with the native element. This test calls the [`DebugElement.triggerEventHandler`](../../api/core/debugelement#triggerEventHandler) with the "click" event name. The "click" event binding responds by calling `DashboardHeroComponent.click()`.

The Angular [`DebugElement.triggerEventHandler`](../../api/core/debugelement#triggerEventHandler) can raise *any data-bound event* by its *event name*. The second parameter is the event object passed to the handler.

The test triggered a "click" event.

```
heroDe.triggerEventHandler('click');
```

In this case, the test correctly assumes that the runtime event handler, the component's `click()` method, doesn't care about the event object.

**HELPFUL:** Other handlers are less forgiving. For example, the [`RouterLink`](../../api/router/routerlink) directive expects an object with a `button` property that identifies which mouse button, if any, was pressed during the click. The [`RouterLink`](../../api/router/routerlink) directive throws an error if the event object is missing.

### Click the element

The following test alternative calls the native element's own `click()` method, which is perfectly fine for *this component*.

```
it('should raise selected event when clicked (element.click)', () => {
    let selectedHero: Hero | undefined;
    comp.selected.subscribe((hero: Hero) => (selectedHero = hero));

    heroEl.click();
    expect(selectedHero).toBe(expectedHero);
  });
```

### click() helper

Clicking a button, an anchor, or an arbitrary HTML element is a common test task.

Make that consistent and straightforward by encapsulating the *click-triggering* process in a helper such as the following `click()` function:

```
/** Button events to pass to `DebugElement.triggerEventHandler` for RouterLink event handler */
export const ButtonClickEvents = {
  left: {button: 0},
  right: {button: 2},
};

/** Simulate element click. Defaults to mouse left-button click event. */
export function click(
  el: DebugElement | HTMLElement,
  eventObj: any = ButtonClickEvents.left,
): void {
  if (el instanceof HTMLElement) {
    el.click();
  } else {
    el.triggerEventHandler('click', eventObj);
  }
}
```

The first parameter is the *element-to-click*. If you want, pass a custom event object as the second parameter. The default is a partial [left-button mouse event object](https://developer.mozilla.org/docs/Web/API/MouseEvent/button) accepted by many handlers including the [`RouterLink`](../../api/router/routerlink) directive.

**IMPORTANT:** The `click()` helper function is **not** one of the Angular testing utilities. It's a function defined in *this guide's sample code*. All of the sample tests use it. If you like it, add it to your own collection of helpers.

Here's the previous test, rewritten using the click helper.

```
it('should raise selected event when clicked (click helper with DebugElement)', () => {
    let selectedHero: Hero | undefined;
    comp.selected.subscribe((hero: Hero) => (selectedHero = hero));

    click(heroDe); // click helper with DebugElement

    expect(selectedHero).toBe(expectedHero);
  });
```

## Component inside a test host

The previous tests played the role of the host `DashboardComponent` themselves. But does the `DashboardHeroComponent` work correctly when properly data-bound to a host component?

```
@Component({
  imports: [DashboardHeroComponent],
  template: ` <dashboard-hero [hero]="hero" (selected)="onSelected($event)"> </dashboard-hero>`,
})
class TestHostComponent {
  hero: Hero = {id: 42, name: 'Test Name'};
  selectedHero: Hero | undefined;
  onSelected(hero: Hero) {
    this.selectedHero = hero;
  }
}
```

The test host sets the component's `hero` input property with its test hero. It binds the component's `selected` event with its `onSelected` handler, which records the emitted hero in its `selectedHero` property.

Later, the tests will be able to check `selectedHero` to verify that the `DashboardHeroComponent.selected` event emitted the expected hero.

The setup for the `test-host` tests is similar to the setup for the stand-alone tests:

```
TestBed.configureTestingModule({
      providers: appProviders,
    });
    // create TestHostComponent instead of DashboardHeroComponent
    fixture = TestBed.createComponent(TestHostComponent);
    testHost = fixture.componentInstance;
    heroEl = fixture.nativeElement.querySelector('.hero');
    fixture.detectChanges(); // trigger initial data binding
```

This testing module configuration shows two important differences:

- It *creates* the `TestHostComponent` instead of the `DashboardHeroComponent`
- The `TestHostComponent` sets the `DashboardHeroComponent.hero` with a binding

The [`createComponent`](../../api/core/createcomponent) returns a `fixture` that holds an instance of `TestHostComponent` instead of an instance of `DashboardHeroComponent`.

Creating the `TestHostComponent` has the side effect of creating a `DashboardHeroComponent` because the latter appears within the template of the former. The query for the hero element (`heroEl`) still finds it in the test DOM, albeit at greater depth in the element tree than before.

The tests themselves are almost identical to the stand-alone version:

```
it('should display hero name', () => {
    const expectedPipedName = testHost.hero.name.toUpperCase();
    expect(heroEl.textContent).toContain(expectedPipedName);
  });

  it('should raise selected event when clicked', () => {
    click(heroEl);
    // selected hero should be the same data bound hero
    expect(testHost.selectedHero).toBe(testHost.hero);
  });
```

Only the selected event test differs. It confirms that the selected `DashboardHeroComponent` hero really does find its way up through the event binding to the host component.

## Routing component

A *routing component* is a component that tells the [`Router`](../../api/router/router) to navigate to another component. The `DashboardComponent` is a *routing component* because the user can navigate to the `HeroDetailComponent` by clicking on one of the *hero buttons* on the dashboard.

Angular provides test helpers to reduce boilerplate and more effectively test code which depends on [`HttpClient`](../../api/common/http/httpclient). The [`provideRouter`](../../api/router/providerouter) function can be used directly in the test module as well.

```
TestBed.configureTestingModule(
      Object.assign({}, appConfig, {
        providers: [
          provideRouter([{path: '**', component: DashboardComponent}]),
          provideHttpClient(),
          provideHttpClientTesting(),
          HeroService,
        ],
      }),
    );
    harness = await RouterTestingHarness.create();
    comp = await harness.navigateByUrl('/', DashboardComponent);
    TestBed.inject(HttpTestingController).expectOne('api/heroes').flush(getTestHeroes());
```

The following test clicks the displayed hero and confirms that we navigate to the expected URL.

```
it('should tell navigate when hero clicked', async () => {
      await heroClick(); // trigger click on first inner <div class="hero">

      // expecting to navigate to id of the component's first hero
      const id = comp.heroes[0].id;
      expect(TestBed.inject(Router).url)
        .withContext('should nav to HeroDetail for first hero')
        .toEqual(`/heroes/${id}`);
    });
```

## Routed components

A *routed component* is the destination of a [`Router`](../../api/router/router) navigation. It can be trickier to test, especially when the route to the component *includes parameters*. The `HeroDetailComponent` is a *routed component* that is the destination of such a route.

When a user clicks a *Dashboard* hero, the `DashboardComponent` tells the [`Router`](../../api/router/router) to navigate to `heroes/:id`. The `:id` is a route parameter whose value is the `id` of the hero to edit.

The [`Router`](../../api/router/router) matches that URL to a route to the `HeroDetailComponent`. It creates an [`ActivatedRoute`](../../api/router/activatedroute) object with the routing information and injects it into a new instance of the `HeroDetailComponent`.

Here are the services injected into `HeroDetailComponent`:

```
private heroDetailService = inject(HeroDetailService);
  private route = inject(ActivatedRoute);
  private router = inject(Router);
```

The `HeroDetail` component needs the `id` parameter so it can fetch the corresponding hero using the `HeroDetailService`. The component has to get the `id` from the [`ActivatedRoute.paramMap`](../../api/router/activatedroute#paramMap) property which is an `Observable`.

It can't just reference the `id` property of the [`ActivatedRoute.paramMap`](../../api/router/activatedroute#paramMap). The component has to *subscribe* to the [`ActivatedRoute.paramMap`](../../api/router/activatedroute#paramMap) observable and be prepared for the `id` to change during its lifetime.

```
constructor() {
    // get hero when `id` param changes
    this.route.paramMap.subscribe((pmap) => this.getHero(pmap.get('id')));
  }
```

Tests can explore how the `HeroDetailComponent` responds to different `id` parameter values by navigating to different routes.

## Nested component tests

Component templates often have nested components, whose templates might contain more components.

The component tree can be very deep and sometimes the nested components play no role in testing the component at the top of the tree.

The `AppComponent`, for example, displays a navigation bar with anchors and their [`RouterLink`](../../api/router/routerlink) directives.

```
<app-banner />
<app-welcome />
<nav>
  <a routerLink="/dashboard">Dashboard</a>
  <a routerLink="/heroes">Heroes</a>
  <a routerLink="/about">About</a>
</nav>
<router-outlet />
```

To validate the links but not the navigation, you don't need the [`Router`](../../api/router/router) to navigate and you don't need the `<router-outlet>` to mark where the [`Router`](../../api/router/router) inserts *routed components*.

The `BannerComponent` and `WelcomeComponent` (indicated by `<app-banner>` and `<app-welcome>`) are also irrelevant.

Yet any test that creates the `AppComponent` in the DOM also creates instances of these three components and, if you let that happen, you'll have to configure the [`TestBed`](../../api/core/testing/testbed) to create them.

If you neglect to declare them, the Angular compiler won't recognize the `<app-banner>`, `<app-welcome>`, and `<router-outlet>` tags in the `AppComponent` template and will throw an error.

If you declare the real components, you'll also have to declare *their* nested components and provide for *all* services injected in *any* component in the tree.

This section describes two techniques for minimizing the setup. Use them, alone or in combination, to stay focused on testing the primary component.

### Stubbing unneeded components

In the first technique, you create and declare stub versions of the components and directive that play little or no role in the tests.

```
@Component({selector: 'app-banner', template: ''})
class BannerStubComponent {}

@Component({selector: 'router-outlet', template: ''})
class RouterOutletStubComponent {}

@Component({selector: 'app-welcome', template: ''})
class WelcomeStubComponent {}
```

The stub selectors match the selectors for the corresponding real components. But their templates and classes are empty.

Then declare them by overriding the `imports` of your component using [`TestBed.overrideComponent`](../../api/core/testing/testbed#overrideComponent).

```
TestBed.configureTestingModule(
      Object.assign({}, appConfig, {
        providers: [provideRouter([]), UserService],
      }),
    ).overrideComponent(AppComponent, {
      set: {
        imports: [BannerStubComponent, RouterLink, RouterOutletStubComponent, WelcomeStubComponent],
      },
    });
```

**HELPFUL:** The `set` key in this example replaces all the exisiting imports on your component, make sure to imports all dependencies, not only the stubs. Alternatively you can use the `remove`/`add` keys to selectively remove and add imports.

### NO\_ERRORS\_SCHEMA

In the second approach, add [`NO_ERRORS_SCHEMA`](../../api/core/no_errors_schema) to the metadata overrides of your component.

```
TestBed.configureTestingModule(
      Object.assign({}, appConfig, {
        providers: [provideRouter([]), UserService],
      }),
    ).overrideComponent(AppComponent, {
      set: {
        imports: [], // resets all imports
        schemas: [NO_ERRORS_SCHEMA],
      },
    });
```

The [`NO_ERRORS_SCHEMA`](../../api/core/no_errors_schema) tells the Angular compiler to ignore unrecognized elements and attributes.

The compiler recognizes the `<app-root>` element and the `routerLink` attribute because you declared a corresponding `AppComponent` and [`RouterLink`](../../api/router/routerlink) in the [`TestBed`](../../api/core/testing/testbed) configuration.

But the compiler won't throw an error when it encounters `<app-banner>`, `<app-welcome>`, or `<router-outlet>`. It simply renders them as empty tags and the browser ignores them.

You no longer need the stub components.

### Use both techniques together

These are techniques for *Shallow Component Testing*, so-named because they reduce the visual surface of the component to just those elements in the component's template that matter for tests.

The [`NO_ERRORS_SCHEMA`](../../api/core/no_errors_schema) approach is the easier of the two but don't overuse it.

The [`NO_ERRORS_SCHEMA`](../../api/core/no_errors_schema) also prevents the compiler from telling you about the missing components and attributes that you omitted inadvertently or misspelled. You could waste hours chasing phantom bugs that the compiler would have caught in an instant.

The *stub component* approach has another advantage. While the stubs in *this* example were empty, you could give them stripped-down templates and classes if your tests need to interact with them in some way.

In practice you will combine the two techniques in the same setup, as seen in this example.

```
TestBed.configureTestingModule(
      Object.assign({}, appConfig, {
        providers: [provideRouter([]), UserService],
      }),
    ).overrideComponent(AppComponent, {
      remove: {
        imports: [RouterOutlet, WelcomeComponent],
      },
      set: {
        schemas: [NO_ERRORS_SCHEMA],
      },
    });
```

The Angular compiler creates the `BannerStubComponent` for the `<app-banner>` element and applies the [`RouterLink`](../../api/router/routerlink) to the anchors with the `routerLink` attribute, but it ignores the `<app-welcome>` and `<router-outlet>` tags.

### By.directive and injected directives

A little more setup triggers the initial data binding and gets references to the navigation links:

```
beforeEach(() => {
    fixture.detectChanges(); // trigger initial data binding

    // find DebugElements with an attached RouterLinkStubDirective
    linkDes = fixture.debugElement.queryAll(By.directive(RouterLink));

    // get attached link directive instances
    // using each DebugElement's injector
    routerLinks = linkDes.map((de) => de.injector.get(RouterLink));
  });
```

Three points of special interest:

- Locate the anchor elements with an attached directive using [`By.directive`](../../api/platform-browser/by#directive)
- The query returns [`DebugElement`](../../api/core/debugelement) wrappers around the matching elements
- Each [`DebugElement`](../../api/core/debugelement) exposes a dependency injector with the specific instance of the directive attached to that element

The `AppComponent` links to validate are as follows:

```
<nav>
  <a routerLink="/dashboard">Dashboard</a>
  <a routerLink="/heroes">Heroes</a>
  <a routerLink="/about">About</a>
</nav>
```

Here are some tests that confirm those links are wired to the `routerLink` directives as expected:

```
it('can get RouterLinks from template', () => {
    expect(routerLinks.length).withContext('should have 3 routerLinks').toBe(3);
    expect(routerLinks[0].href).toBe('/dashboard');
    expect(routerLinks[1].href).toBe('/heroes');
    expect(routerLinks[2].href).toBe('/about');
  });

  it('can click Heroes link in template', fakeAsync(() => {
    const heroesLinkDe = linkDes[1]; // heroes link DebugElement

    TestBed.inject(Router).resetConfig([{path: '**', children: []}]);
    heroesLinkDe.triggerEventHandler('click', {button: 0});
    tick();
    fixture.detectChanges();

    expect(TestBed.inject(Router).url).toBe('/heroes');
  }));
```

## Use a page object

The `HeroDetailComponent` is a simple view with a title, two hero fields, and two buttons.

But there's plenty of template complexity even in this simple form.

```
@if (hero) {
  <div>
    <h2>
      <span>{{ hero.name | titlecase }}</span> Details
    </h2>
    <div><span>id: </span>{{ hero.id }}</div>
    <div>
      <label for="name">name: </label>
      <input id="name" [(ngModel)]="hero.name" placeholder="name" />
    </div>
    <button type="button" (click)="save()">Save</button>
    <button type="button" (click)="cancel()">Cancel</button>
  </div>
}
```

Tests that exercise the component need …

- To wait until a hero arrives before elements appear in the DOM
- A reference to the title text
- A reference to the name input box to inspect and set it
- References to the two buttons so they can click them

Even a small form such as this one can produce a mess of tortured conditional setup and CSS element selection.

Tame the complexity with a `Page` class that handles access to component properties and encapsulates the logic that sets them.

Here is such a `Page` class for the `hero-detail.component.spec.ts`

```
class Page {
  // getter properties wait to query the DOM until called.
  get buttons() {
    return this.queryAll<HTMLButtonElement>('button');
  }
  get saveBtn() {
    return this.buttons[0];
  }
  get cancelBtn() {
    return this.buttons[1];
  }
  get nameDisplay() {
    return this.query<HTMLElement>('span');
  }
  get nameInput() {
    return this.query<HTMLInputElement>('input');
  }

  //// query helpers ////
  private query<T>(selector: string): T {
    return harness.routeNativeElement!.querySelector(selector)! as T;
  }

  private queryAll<T>(selector: string): T[] {
    return harness.routeNativeElement!.querySelectorAll(selector) as any as T[];
  }
}
```

Now the important hooks for component manipulation and inspection are neatly organized and accessible from an instance of `Page`.

A [`createComponent`](../../api/core/createcomponent) method creates a `page` object and fills in the blanks once the `hero` arrives.

```
async function createComponent(id: number) {
  harness = await RouterTestingHarness.create();
  component = await harness.navigateByUrl(`/heroes/${id}`, HeroDetailComponent);
  page = new Page();

  const request = TestBed.inject(HttpTestingController).expectOne(`api/heroes/?id=${id}`);
  const hero = getTestHeroes().find((h) => h.id === Number(id));
  request.flush(hero ? [hero] : []);
  harness.detectChanges();
}
```

Here are a few more `HeroDetailComponent` tests to reinforce the point.

```
it("should display that hero's name", () => {
      expect(page.nameDisplay.textContent).toBe(expectedHero.name);
    });

    it('should navigate when click cancel', () => {
      click(page.cancelBtn);
      expect(TestBed.inject(Router).url).toEqual(`/heroes/${expectedHero.id}`);
    });

    it('should save when click save but not navigate immediately', () => {
      click(page.saveBtn);
      expect(TestBed.inject(HttpTestingController).expectOne({method: 'PUT', url: 'api/heroes'}));
      expect(TestBed.inject(Router).url).toEqual('/heroes/41');
    });

    it('should navigate when click save and save resolves', fakeAsync(() => {
      click(page.saveBtn);
      tick(); // wait for async save to complete
      expect(TestBed.inject(Router).url).toEqual('/heroes/41');
    }));

    it('should convert hero name to Title Case', async () => {
      harness.fixture.autoDetectChanges();
      // get the name's input and display elements from the DOM
      const hostElement: HTMLElement = harness.routeNativeElement!;
      const nameInput: HTMLInputElement = hostElement.querySelector('input')!;
      const nameDisplay: HTMLElement = hostElement.querySelector('span')!;

      // simulate user entering a new name into the input box
      nameInput.value = 'quick BROWN  fOx';

      // Dispatch a DOM event so that Angular learns of input value change.
      nameInput.dispatchEvent(new Event('input'));

      // Wait for Angular to update the display binding through the title pipe
      await harness.fixture.whenStable();

      expect(nameDisplay.textContent).toBe('Quick Brown  Fox');
    });
```

## Override component providers

The `HeroDetailComponent` provides its own `HeroDetailService`.

```
@Component({
  selector: 'app-hero-detail',
  templateUrl: './hero-detail.component.html',
  styleUrls: ['./hero-detail.component.css'],
  providers: [HeroDetailService],
  imports: [...sharedImports],
})
export class HeroDetailComponent {
  private heroDetailService = inject(HeroDetailService);
  private route = inject(ActivatedRoute);
  private router = inject(Router);
}
```

It's not possible to stub the component's `HeroDetailService` in the `providers` of the [`TestBed.configureTestingModule`](../../api/core/testing/testbed#configureTestingModule). Those are providers for the *testing module*, not the component. They prepare the dependency injector at the *fixture level*.

Angular creates the component with its *own* injector, which is a *child* of the fixture injector. It registers the component's providers (the `HeroDetailService` in this case) with the child injector.

A test cannot get to child injector services from the fixture injector. And [`TestBed.configureTestingModule`](../../api/core/testing/testbed#configureTestingModule) can't configure them either.

Angular has created new instances of the real `HeroDetailService` all along!

**HELPFUL:** These tests could fail or timeout if the `HeroDetailService` made its own XHR calls to a remote server. There might not be a remote server to call.

Fortunately, the `HeroDetailService` delegates responsibility for remote data access to an injected `HeroService`.

```
@Injectable({providedIn: 'root'})
export class HeroDetailService {
  private heroService = inject(HeroService);
  /* . . . */
}
```

The previous test configuration replaces the real `HeroService` with a `TestHeroService` that intercepts server requests and fakes their responses.

What if you aren't so lucky. What if faking the `HeroService` is hard? What if `HeroDetailService` makes its own server requests?

The [`TestBed.overrideComponent`](../../api/core/testing/testbed#overrideComponent) method can replace the component's `providers` with easy-to-manage *test doubles* as seen in the following setup variation:

```
beforeEach(async () => {
    await TestBed.configureTestingModule(
      Object.assign({}, appConfig, {
        imports: [HeroDetailComponent, HeroListComponent],
        providers: [
          provideRouter([
            {path: 'heroes', component: HeroListComponent},
            {path: 'heroes/:id', component: HeroDetailComponent},
          ]),
          HttpClient,
          HttpHandler,
          // HeroDetailService at this level is IRRELEVANT!
          {provide: HeroDetailService, useValue: {}},
        ],
      }),
    )
      .overrideComponent(HeroDetailComponent, {
        set: {providers: [{provide: HeroDetailService, useClass: HeroDetailServiceSpy}]},
      });
  });
```

Notice that [`TestBed.configureTestingModule`](../../api/core/testing/testbed#configureTestingModule) no longer provides a fake `HeroService` because it's [not needed](#provide-a-spy-stub-herodetailservicespy).

### The overrideComponent method

Focus on the `overrideComponent` method.

```
.overrideComponent(HeroDetailComponent, {
        set: {providers: [{provide: HeroDetailService, useClass: HeroDetailServiceSpy}]},
      });
```

It takes two arguments: the component type to override (`HeroDetailComponent`) and an override metadata object. The [override metadata object](utility-apis#metadata-override-object) is a generic defined as follows:

```
type MetadataOverride<T> = {
add?: Partial<T>;
remove?: Partial<T>;
set?: Partial<T>;
};
```

A metadata override object can either add-and-remove elements in metadata properties or completely reset those properties. This example resets the component's `providers` metadata.

The type parameter, `T`, is the kind of metadata you'd pass to the [`@Component`](../../api/core/component) decorator:

```
selector?: string;
template?: string;
templateUrl?: string;
providers?: any[];
…
```

### Provide a spy stub (HeroDetailServiceSpy)

This example completely replaces the component's `providers` array with a new array containing a `HeroDetailServiceSpy`.

The `HeroDetailServiceSpy` is a stubbed version of the real `HeroDetailService` that fakes all necessary features of that service. It neither injects nor delegates to the lower level `HeroService` so there's no need to provide a test double for that.

The related `HeroDetailComponent` tests will assert that methods of the `HeroDetailService` were called by spying on the service methods. Accordingly, the stub implements its methods as spies:

```
class HeroDetailServiceSpy {
    testHero: Hero = {...testHero};

    /* emit cloned test hero */
    getHero = jasmine
      .createSpy('getHero')
      .and.callFake(() => asyncData(Object.assign({}, this.testHero)));

    /* emit clone of test hero, with changes merged in */
    saveHero = jasmine
      .createSpy('saveHero')
      .and.callFake((hero: Hero) => asyncData(Object.assign(this.testHero, hero)));
  }
```

### The override tests

Now the tests can control the component's hero directly by manipulating the spy-stub's `testHero` and confirm that service methods were called.

```
let hdsSpy: HeroDetailServiceSpy;

  beforeEach(async () => {
    harness = await RouterTestingHarness.create();
    component = await harness.navigateByUrl(`/heroes/${testHero.id}`, HeroDetailComponent);
    page = new Page();
    // get the component's injected HeroDetailServiceSpy
    hdsSpy = harness.routeDebugElement!.injector.get(HeroDetailService) as any;

    harness.detectChanges();
  });

  it('should have called `getHero`', () => {
    expect(hdsSpy.getHero.calls.count())
      .withContext('getHero called once')
      .toBe(1, 'getHero called once');
  });

  it("should display stub hero's name", () => {
    expect(page.nameDisplay.textContent).toBe(hdsSpy.testHero.name);
  });

  it('should save stub hero change', fakeAsync(() => {
    const origName = hdsSpy.testHero.name;
    const newName = 'New Name';

    page.nameInput.value = newName;

    page.nameInput.dispatchEvent(new Event('input')); // tell Angular

    expect(component.hero.name).withContext('component hero has new name').toBe(newName);
    expect(hdsSpy.testHero.name).withContext('service hero unchanged before save').toBe(origName);

    click(page.saveBtn);
    expect(hdsSpy.saveHero.calls.count()).withContext('saveHero called once').toBe(1);

    tick(); // wait for async save to complete
    expect(hdsSpy.testHero.name).withContext('service hero has new name after save').toBe(newName);
    expect(TestBed.inject(Router).url).toEqual('/heroes');
  }));
}
```

### More overrides

The [`TestBed.overrideComponent`](../../api/core/testing/testbed#overrideComponent) method can be called multiple times for the same or different components. The [`TestBed`](../../api/core/testing/testbed) offers similar `overrideDirective`, `overrideModule`, and `overridePipe` methods for digging into and replacing parts of these other classes.

Explore the options and combinations on your own.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/testing/components-scenarios>
