# Testing Utility APIs

Testing Utility APIs



# Testing Utility APIs

  

**NOTE:** While this guide is being updated for Vitest, some descriptions and examples of utility APIs are currently presented within the context of Karma/Jasmine. We are actively working to provide Vitest equivalents and updated guidance where applicable.

This page describes the most useful Angular testing features.

The Angular testing utilities include the [`TestBed`](../../api/core/testing/testbed), the [`ComponentFixture`](../../api/core/testing/componentfixture), and a handful of functions that control the test environment. The [`TestBed`](../../api/core/testing/testbed) and [`ComponentFixture`](../../api/core/testing/componentfixture) classes are covered separately.

Here's a summary of the stand-alone functions, in order of likely utility:

| Function | Details |
| --- | --- |
| `inject` | Injects one or more services from the current [`TestBed`](../../api/core/testing/testbed) injector into a test function. It cannot inject a service provided by the component itself. See discussion of the [debugElement.injector](components-scenarios#get-injected-services). |
| [`ComponentFixtureAutoDetect`](../../api/core/testing/componentfixtureautodetect) | A provider token for a service that turns on [automatic change detection](components-scenarios#automatic-change-detection). |
| [`getTestBed`](../../api/core/testing/gettestbed) | Gets the current instance of the [`TestBed`](../../api/core/testing/testbed). Usually unnecessary because the static class methods of the [`TestBed`](../../api/core/testing/testbed) class are typically sufficient. The [`TestBed`](../../api/core/testing/testbed) instance exposes a few rarely used members that are not available as static methods. |

For handling complex asynchronous scenarios or testing legacy Zone.js-based applications, see the [Zone.js Testing Utilities](zone-js-testing-utilities) guide.

## TestBed class summary

The [`TestBed`](../../api/core/testing/testbed) class is one of the principal Angular testing utilities. Its API is quite large and can be overwhelming until you've explored it, a little at a time. Read the early part of this guide first to get the basics before trying to absorb the full API.

The module definition passed to `configureTestingModule` is a subset of the [`@NgModule`](../../api/core/ngmodule) metadata properties.

```
type TestModuleMetadata = {
providers?: any[];
declarations?: any[];
imports?: any[];
schemas?: Array<SchemaMetadata | any[]>;
};
```

Each override method takes a `MetadataOverride<T>` where `T` is the kind of metadata appropriate to the method, that is, the parameter of an [`@NgModule`](../../api/core/ngmodule), [`@Component`](../../api/core/component), [`@Directive`](../../api/core/directive), or [`@Pipe`](../../api/core/pipe).

```
type MetadataOverride<T> = {
add?: Partial<T>;
remove?: Partial<T>;
set?: Partial<T>;
};
```

The [`TestBed`](../../api/core/testing/testbed) API consists of static class methods that either update or reference a *global* instance of the [`TestBed`](../../api/core/testing/testbed).

Internally, all static methods cover methods of the current runtime [`TestBed`](../../api/core/testing/testbed) instance, which is also returned by the [`getTestBed()`](../../api/core/testing/gettestbed) function.

Call [`TestBed`](../../api/core/testing/testbed) methods *within* a `beforeEach()` to ensure a fresh start before each individual test.

Here are the most important static methods, in order of likely utility.

| Methods | Details |
| --- | --- |
| `configureTestingModule` | The testing shims establish the [initial test environment](../testing) and a default testing module. The default testing module is configured with basic declaratives and some Angular service substitutes that every tester needs.   Call `configureTestingModule` to refine the testing module configuration for a particular set of tests by adding and removing imports, declarations (of components, directives, and pipes), and providers. |
| `compileComponents` | Compile the testing module asynchronously after you've finished configuring it. You **must** call this method if *any* of the testing module components have a `templateUrl` or `styleUrls` because fetching component template and style files is necessarily asynchronous. See [compileComponents](components-scenarios#calling-compilecomponents).   After calling `compileComponents`, the [`TestBed`](../../api/core/testing/testbed) configuration is frozen for the duration of the current spec. |
| `createComponent<T>` | Create an instance of a component of type `T` based on the current [`TestBed`](../../api/core/testing/testbed) configuration. After calling [`createComponent`](../../api/core/createcomponent), the [`TestBed`](../../api/core/testing/testbed) configuration is frozen for the duration of the current spec. |
| `overrideModule` | Replace metadata for the given [`NgModule`](../../api/core/ngmodule). Recall that modules can import other modules. The `overrideModule` method can reach deeply into the current testing module to modify one of these inner modules. |
| `overrideComponent` | Replace metadata for the given component class, which could be nested deeply within an inner module. |
| `overrideDirective` | Replace metadata for the given directive class, which could be nested deeply within an inner module. |
| `overridePipe` | Replace metadata for the given pipe class, which could be nested deeply within an inner module. |

| `inject` | Retrieve a service from the current [`TestBed`](../../api/core/testing/testbed) injector. The `inject` function is often adequate for this purpose. But `inject` throws an error if it can't provide the service.   
 What if the service is optional?   
 The [`TestBed.inject()`](../../api/core/testing/testbed#inject) method takes an optional second parameter, the object to return if Angular can't find the provider (`null` in this example):  After calling [`TestBed.inject`](../../api/core/testing/testbed#inject), the [`TestBed`](../../api/core/testing/testbed) configuration is frozen for the duration of the current spec. | | `initTestEnvironment` | Initialize the testing environment for the entire test run.   
 The testing shims call it for you so there is rarely a reason for you to call it yourself.   
 Call this method *exactly once*. To change this default in the middle of a test run, call `resetTestEnvironment` first.   
 Specify the Angular compiler factory, a [`PlatformRef`](../../api/core/platformref), and a default Angular testing module. Alternatives for non-browser platforms are available in the general form `@angular/platform-<platform_name>/testing/<platform_name>`. | | `resetTestEnvironment` | Reset the initial test environment, including the default testing module. |

A few of the [`TestBed`](../../api/core/testing/testbed) instance methods are not covered by static [`TestBed`](../../api/core/testing/testbed) *class* methods. These are rarely needed.

## The ComponentFixture

The [`TestBed.createComponent<T>`](#) creates an instance of the component `T` and returns a strongly typed [`ComponentFixture`](../../api/core/testing/componentfixture) for that component.

The [`ComponentFixture`](../../api/core/testing/componentfixture) properties and methods provide access to the component, its DOM representation, and aspects of its Angular environment.

### ComponentFixture properties

Here are the most important properties for testers, in order of likely utility.

| Properties | Details |
| --- | --- |
| `componentInstance` | The instance of the component class created by [`TestBed.createComponent`](../../api/core/testing/testbed#createComponent). |
| `debugElement` | The [`DebugElement`](../../api/core/debugelement) associated with the root element of the component.   The `debugElement` provides insight into the component and its DOM element during test and debugging. It's a critical property for testers. The most interesting members are covered [below](#debugelement). |
| `nativeElement` | The native DOM element at the root of the component. |
| `changeDetectorRef` | The [`ChangeDetectorRef`](../../api/core/changedetectorref) for the component.   The [`ChangeDetectorRef`](../../api/core/changedetectorref) is most valuable when testing a component that has the [`ChangeDetectionStrategy.OnPush`](../../api/core/changedetectionstrategy#OnPush) method or the component's change detection is under your programmatic control. |

### ComponentFixture methods

The *fixture* methods cause Angular to perform certain tasks on the component tree. Call these method to trigger Angular behavior in response to simulated user action.

Here are the most useful methods for testers.

| Methods | Details |
| --- | --- |
| `detectChanges` | Trigger a change detection cycle for the component.   Call it to initialize the component (it calls `ngOnInit`) and after your test code, change the component's data bound property values. Angular can't see that you've changed `personComponent.name` and won't update the `name` binding until you call `detectChanges`.   Runs `checkNoChanges` afterwards to confirm that there are no circular updates unless called as `detectChanges(false)`; |
| `autoDetectChanges` | Set this to `true` when you want the fixture to detect changes automatically.   When autodetect is `true`, the test fixture calls `detectChanges` immediately after creating the component. Then it listens for pertinent zone events and calls `detectChanges` accordingly. When your test code modifies component property values directly, you probably still have to call `fixture.detectChanges` to trigger data binding updates.   The default is `false`. Testers who prefer fine control over test behavior tend to keep it `false`. |
| `checkNoChanges` | Do a change detection run to make sure there are no pending changes. Throws an exceptions if there are. |
| `isStable` | If the fixture is currently *stable*, returns `true`. If there are async tasks that have not completed, returns `false`. |
| `whenStable` | Returns a promise that resolves when the fixture is stable.   To resume testing after completion of asynchronous activity or asynchronous change detection, hook that promise. See [whenStable](components-scenarios#whenstable). |
| `destroy` | Trigger component destruction. |

#### DebugElement

The [`DebugElement`](../../api/core/debugelement) provides crucial insights into the component's DOM representation.

From the test root component's [`DebugElement`](../../api/core/debugelement) returned by `fixture.debugElement`, you can walk (and query) the fixture's entire element and component subtrees.

Here are the most useful [`DebugElement`](../../api/core/debugelement) members for testers, in approximate order of utility:

| Members | Details |
| --- | --- |
| `nativeElement` | The corresponding DOM element in the browser |
| [`query`](../../api/animations/query) | Calling `query(predicate: Predicate<DebugElement>)` returns the first [`DebugElement`](../../api/core/debugelement) that matches the predicate at any depth in the subtree. |
| `queryAll` | Calling `queryAll(predicate: Predicate<DebugElement>)` returns all `DebugElements` that matches the predicate at any depth in subtree. |
| `injector` | The host dependency injector. For example, the root element's component instance injector. |
| `componentInstance` | The element's own component instance, if it has one. |
| `context` | An object that provides parent context for this element. Often an ancestor component instance that governs this element.   When an element is repeated within `@for` block, the context is an `RepeaterContext` whose `$implicit` property is the value of the row instance value. For example, the `hero` in `@for(hero of heroes; ...)`. |
| `children` | The immediate [`DebugElement`](../../api/core/debugelement) children. Walk the tree by descending through `children`. [`DebugElement`](../../api/core/debugelement) also has `childNodes`, a list of [`DebugNode`](../../api/core/debugnode) objects. [`DebugElement`](../../api/core/debugelement) derives from [`DebugNode`](../../api/core/debugnode) objects and there are often more nodes than elements. Testers can usually ignore plain nodes. |
| `parent` | The [`DebugElement`](../../api/core/debugelement) parent. Null if this is the root element. |
| `name` | The element tag name, if it is an element. |
| `triggerEventHandler` | Triggers the event by its name if there is a corresponding listener in the element's `listeners` collection. The second parameter is the *event object* expected by the handler. See [triggerEventHandler](components-scenarios#trigger-event-handler).   If the event lacks a listener or there's some other problem, consider calling `nativeElement.dispatchEvent(eventObject)`. |
| `listeners` | The callbacks attached to the component's [`@Output`](../../api/core/output) properties and/or the element's event properties. |
| `providerTokens` | This component's injector lookup tokens. Includes the component itself plus the tokens that the component lists in its `providers` metadata. |
| `source` | Where to find this element in the source component template. |
| `references` | Dictionary of objects associated with template local variables (for example, `#foo`), keyed by the local variable name. |

The [`DebugElement.query(predicate)`](../../api/core/debugelement#query(predicate)) and [`DebugElement.queryAll(predicate)`](../../api/core/debugelement#queryAll(predicate)) methods take a predicate that filters the source element's subtree for matching [`DebugElement`](../../api/core/debugelement).

The predicate is any method that takes a [`DebugElement`](../../api/core/debugelement) and returns a *truthy* value. The following example finds all `DebugElements` with a reference to a template local variable named "content":

```
// Filter for DebugElements with a #content reference
      const contentRefs = el.queryAll((de) => de.references['content']);
```

The Angular [`By`](../../api/platform-browser/by) class has three static methods for common predicates:

| Static method | Details |
| --- | --- |
| [`By.all`](../../api/platform-browser/by#all) | Return all elements |
| [`By.css(selector)`](../../api/platform-browser/by#css(selector)) | Return elements with matching CSS selectors |
| [`By.directive(directive)`](../../api/platform-browser/by#directive(directive)) | Return elements that Angular matched to an instance of the directive class |

```
// Can find DebugElement either by css selector or by directive
    const h2 = fixture.debugElement.query(By.css('h2'));
    const directive = fixture.debugElement.query(By.directive(HighlightDirective));
```

Super-powered by Google ©2010–2025.
