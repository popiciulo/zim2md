# Basics of testing components

Basics of testing components



# Basics of testing components

  

A component, unlike all other parts of an Angular application, combines an HTML template and a TypeScript class. The component truly is the template and the class *working together*. To adequately test a component, you should test that they work together as intended.

Such tests require creating the component's host element in the browser DOM, as Angular does, and investigating the component class's interaction with the DOM as described by its template.

The Angular [`TestBed`](../../api/core/testing/testbed) facilitates this kind of testing as you'll see in the following sections. But in many cases, *testing the component class alone*, without DOM involvement, can validate much of the component's behavior in a straightforward, more obvious way.

## Component DOM testing

A component is more than just its class. A component interacts with the DOM and with other components. Classes alone cannot tell you if the component is going to render properly, respond to user input and gestures, or integrate with its parent and child components.

- Is `Lightswitch.clicked()` bound to anything such that the user can invoke it?
- Is the `Lightswitch.message` displayed?
- Can the user actually select the hero displayed by `DashboardHeroComponent`?
- Is the hero name displayed as expected (such as uppercase)?
- Is the welcome message displayed by the template of `WelcomeComponent`?

These might not be troubling questions for the preceding simple components illustrated. But many components have complex interactions with the DOM elements described in their templates, causing HTML to appear and disappear as the component state changes.

To answer these kinds of questions, you have to create the DOM elements associated with the components, you must examine the DOM to confirm that component state displays properly at the appropriate times, and you must simulate user interaction with the screen to determine whether those interactions cause the component to behave as expected.

To write these kinds of test, you'll use additional features of the [`TestBed`](../../api/core/testing/testbed) as well as other testing helpers.

### CLI-generated tests

The CLI creates an initial test file for you by default when you ask it to generate a new component.

For example, the following CLI command generates a `BannerComponent` in the `app/banner` folder (with inline template and styles):

```
ng generate component banner --inline-template --inline-style --module app
```

It also generates an initial test file for the component, `banner-external.component.spec.ts`, that looks like this:

```
import {ComponentFixture, TestBed, waitForAsync} from '@angular/core/testing';

import { BannerComponent } from './banner.component';

describe('BannerComponent', () => {
  let component: BannerComponent;
  let fixture: ComponentFixture<BannerComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({imports: [BannerComponent]});
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeDefined();
  });
});
```

**HELPFUL:** Because `compileComponents` is asynchronous, it uses the [`waitForAsync`](../../api/core/testing/waitforasync) utility function imported from `@angular/core/testing`.

Refer to the [waitForAsync](components-scenarios#waitForAsync) section for more details.

### Reduce the setup

Only the last three lines of this file actually test the component and all they do is assert that Angular can create the component.

The rest of the file is boilerplate setup code anticipating more advanced tests that *might* become necessary if the component evolves into something substantial.

You'll learn about these advanced test features in the following sections. For now, you can radically reduce this test file to a more manageable size:

```
describe('BannerComponent (minimal)', () => {
  it('should create', () => {
    TestBed.configureTestingModule({imports: [BannerComponent]});
    const fixture = TestBed.createComponent(BannerComponent);
    const component = fixture.componentInstance;
    expect(component).toBeDefined();
  });
});
```

In this example, the metadata object passed to [`TestBed.configureTestingModule`](../../api/core/testing/testbed#configureTestingModule) simply declares `BannerComponent`, the component to test.

```
TestBed.configureTestingModule({imports: [BannerComponent]});
```

**HELPFUL:** There's no need to declare or import anything else. The default test module is pre-configured with something like the [`BrowserModule`](../../api/platform-browser/browsermodule) from `@angular/platform-browser`.

Later you'll call [`TestBed.configureTestingModule()`](../../api/core/testing/testbed#configureTestingModule) with imports, providers, and more declarations to suit your testing needs. Optional `override` methods can further fine-tune aspects of the configuration.

### createComponent()

After configuring [`TestBed`](../../api/core/testing/testbed), you call its [`createComponent()`](../../api/core/createcomponent) method.

```
const fixture = TestBed.createComponent(BannerComponent);
```

[`TestBed.createComponent()`](../../api/core/testing/testbed#createComponent) creates an instance of the `BannerComponent`, adds a corresponding element to the test-runner DOM, and returns a [`ComponentFixture`](../../api/core/testing/componentfixture).

**IMPORTANT:** Do not re-configure [`TestBed`](../../api/core/testing/testbed) after calling [`createComponent`](../../api/core/createcomponent).

The [`createComponent`](../../api/core/createcomponent) method freezes the current [`TestBed`](../../api/core/testing/testbed) definition, closing it to further configuration.

You cannot call any more [`TestBed`](../../api/core/testing/testbed) configuration methods, not `configureTestingModule()`, nor `get()`, nor any of the `override...` methods. If you try, [`TestBed`](../../api/core/testing/testbed) throws an error.

### ComponentFixture

The [ComponentFixture](../../api/core/testing/componentfixture) is a test harness for interacting with the created component and its corresponding element.

Access the component instance through the fixture and confirm it exists with a Jasmine expectation:

```
const component = fixture.componentInstance;
    expect(component).toBeDefined();
```

### beforeEach()

You will add more tests as this component evolves. Rather than duplicate the [`TestBed`](../../api/core/testing/testbed) configuration for each test, you refactor to pull the setup into a Jasmine `beforeEach()` and some supporting variables:

```
describe('BannerComponent (with beforeEach)', () => {
  let component: BannerComponent;
  let fixture: ComponentFixture<BannerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({imports: [BannerComponent]});
    fixture = TestBed.createComponent(BannerComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeDefined();
  });
});
```

Now add a test that gets the component's element from `fixture.nativeElement` and looks for the expected text.

```
it('should contain "banner works!"', () => {
    const bannerElement: HTMLElement = fixture.nativeElement;
    expect(bannerElement.textContent).toContain('banner works!');
  });
```

### nativeElement

The value of [`ComponentFixture.nativeElement`](../../api/core/testing/componentfixture#nativeElement) has the `any` type. Later you'll encounter the [`DebugElement.nativeElement`](../../api/core/debugelement#nativeElement) and it too has the `any` type.

Angular can't know at compile time what kind of HTML element the `nativeElement` is or if it even is an HTML element. The application might be running on a *non-browser platform*, such as the server or a [Web Worker](https://developer.mozilla.org/docs/Web/API/Web_Workers_API), where the element might have a diminished API or not exist at all.

The tests in this guide are designed to run in a browser so a `nativeElement` value will always be an `HTMLElement` or one of its derived classes.

Knowing that it is an `HTMLElement` of some sort, use the standard HTML `querySelector` to dive deeper into the element tree.

Here's another test that calls `HTMLElement.querySelector` to get the paragraph element and look for the banner text:

```
it('should have <p> with "banner works!"', () => {
    const bannerElement: HTMLElement = fixture.nativeElement;
    const p = bannerElement.querySelector('p')!;
    expect(p.textContent).toEqual('banner works!');
  });
```

### DebugElement

The Angular *fixture* provides the component's element directly through the `fixture.nativeElement`.

```
const bannerElement: HTMLElement = fixture.nativeElement;
```

This is actually a convenience method, implemented as `fixture.debugElement.nativeElement`.

```
const bannerDe: DebugElement = fixture.debugElement;
    const bannerEl: HTMLElement = bannerDe.nativeElement;
```

There's a good reason for this circuitous path to the element.

The properties of the `nativeElement` depend upon the runtime environment. You could be running these tests on a *non-browser* platform that doesn't have a DOM or whose DOM-emulation doesn't support the full `HTMLElement` API.

Angular relies on the [`DebugElement`](../../api/core/debugelement) abstraction to work safely across *all supported platforms*. Instead of creating an HTML element tree, Angular creates a [`DebugElement`](../../api/core/debugelement) tree that wraps the *native elements* for the runtime platform. The `nativeElement` property unwraps the [`DebugElement`](../../api/core/debugelement) and returns the platform-specific element object.

Because the sample tests for this guide are designed to run only in a browser, a `nativeElement` in these tests is always an `HTMLElement` whose familiar methods and properties you can explore within a test.

Here's the previous test, re-implemented with `fixture.debugElement.nativeElement`:

```
it('should find the <p> with fixture.debugElement.nativeElement', () => {
    const bannerDe: DebugElement = fixture.debugElement;
    const bannerEl: HTMLElement = bannerDe.nativeElement;
    const p = bannerEl.querySelector('p')!;
    expect(p.textContent).toEqual('banner works!');
  });
```

The [`DebugElement`](../../api/core/debugelement) has other methods and properties that are useful in tests, as you'll see elsewhere in this guide.

You import the [`DebugElement`](../../api/core/debugelement) symbol from the Angular core library.

```
import {DebugElement} from '@angular/core';
```

### By.css()

Although the tests in this guide all run in the browser, some applications might run on a different platform at least some of the time.

For example, the component might render first on the server as part of a strategy to make the application launch faster on poorly connected devices. The server-side renderer might not support the full HTML element API. If it doesn't support `querySelector`, the previous test could fail.

The [`DebugElement`](../../api/core/debugelement) offers query methods that work for all supported platforms. These query methods take a *predicate* function that returns `true` when a node in the [`DebugElement`](../../api/core/debugelement) tree matches the selection criteria.

You create a *predicate* with the help of a [`By`](../../api/platform-browser/by) class imported from a library for the runtime platform. Here's the [`By`](../../api/platform-browser/by) import for the browser platform:

```
import {By} from '@angular/platform-browser';
```

The following example re-implements the previous test with [`DebugElement.query()`](../../api/core/debugelement#query) and the browser's [`By.css`](../../api/platform-browser/by#css) method.

```
it('should find the <p> with fixture.debugElement.query(By.css)', () => {
    const bannerDe: DebugElement = fixture.debugElement;
    const paragraphDe = bannerDe.query(By.css('p'));
    const p: HTMLElement = paragraphDe.nativeElement;
    expect(p.textContent).toEqual('banner works!');
  });
```

Some noteworthy observations:

- The [`By.css()`](../../api/platform-browser/by#css) static method selects [`DebugElement`](../../api/core/debugelement) nodes with a [standard CSS selector](https://developer.mozilla.org/docs/Learn/CSS/Building_blocks/Selectors "CSS selectors").
- The query returns a [`DebugElement`](../../api/core/debugelement) for the paragraph.
- You must unwrap that result to get the paragraph element.

When you're filtering by CSS selector and only testing properties of a browser's *native element*, the [`By.css`](../../api/platform-browser/by#css) approach might be overkill.

It's often more straightforward and clear to filter with a standard `HTMLElement` method such as `querySelector()` or `querySelectorAll()`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/testing/components-basics>
