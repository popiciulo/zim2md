# Testing services

Testing services



# Testing services

  

**NOTE:** While this guide is being updated for Vitest, some code examples currently use Karma/Jasmine syntax and APIs. We are actively working to provide Vitest equivalents where applicable.

To check that your services are working as you intend, you can write tests specifically for them.

Services are often the smoothest files to unit test. Here are some synchronous and asynchronous unit tests of the `ValueService` written without assistance from Angular testing utilities.

```
// Straight Jasmine testing without Angular's testing support
  describe('ValueService', () => {
    let service: ValueService;
    beforeEach(() => {
      service = new ValueService();
    });

    it('#getValue should return real value', () => {
      expect(service.getValue()).toBe('real value');
    });

    it('#getObservableValue should return value from observable', (done: DoneFn) => {
      service.getObservableValue().subscribe((value) => {
        expect(value).toBe('observable value');
        done();
      });
    });

    it('#getPromiseValue should return value from a promise', (done: DoneFn) => {
      service.getPromiseValue().then((value) => {
        expect(value).toBe('promise value');
        done();
      });
    });
  });
```

## Testing services with the TestBed

Your application relies on Angular [dependency injection (DI)](../di) to create services. When a service has a dependent service, DI finds or creates that dependent service. And if that dependent service has its own dependencies, DI finds-or-creates them as well.

As a service *consumer*, you don't worry about any of this. You don't worry about the order of constructor arguments or how they're created.

As a service *tester*, you must at least think about the first level of service dependencies but you *can* let Angular DI do the service creation and deal with constructor argument order when you use the [`TestBed`](../../api/core/testing/testbed) testing utility to provide and create services.

## Angular TestBed

The [`TestBed`](../../api/core/testing/testbed) is the most important of the Angular testing utilities. The [`TestBed`](../../api/core/testing/testbed) creates a dynamically-constructed Angular *test* module that emulates an Angular [@NgModule](../ngmodules/overview).

The [`TestBed.configureTestingModule()`](../../api/core/testing/testbed#configureTestingModule) method takes a metadata object that can have most of the properties of an [@NgModule](../ngmodules/overview).

To test a service, you set the `providers` metadata property with an array of the services that you'll test or mock.

```
let service: ValueService;

    beforeEach(() => {
      TestBed.configureTestingModule({providers: [ValueService]});
    });
```

Then inject it inside a test by calling [`TestBed.inject()`](../../api/core/testing/testbed#inject) with the service class as the argument.

**HELPFUL:** [`TestBed.get()`](../../api/core/testing/testbed#get) was deprecated as of Angular version 9. To help minimize breaking changes, Angular introduces a new function called [`TestBed.inject()`](../../api/core/testing/testbed#inject), which you should use instead.

```
it('should use ValueService', () => {
      service = TestBed.inject(ValueService);
      expect(service.getValue()).toBe('real value');
    });
```

Or inside the `beforeEach()` if you prefer to inject the service as part of your setup.

```
beforeEach(() => {
      TestBed.configureTestingModule({providers: [ValueService]});
      service = TestBed.inject(ValueService);
    });
```

When testing a service with a dependency, provide the mock in the `providers` array.

In the following example, the mock is a spy object.

```
let masterService: MasterService;
    let valueServiceSpy: jasmine.SpyObj<ValueService>;

    beforeEach(() => {
      const spy = jasmine.createSpyObj('ValueService', ['getValue']);

      TestBed.configureTestingModule({
        // Provide both the service-to-test and its (spy) dependency
        providers: [MasterService, {provide: ValueService, useValue: spy}],
      });
      // Inject both the service-to-test and its (spy) dependency
      masterService = TestBed.inject(MasterService);
      valueServiceSpy = TestBed.inject(ValueService) as jasmine.SpyObj<ValueService>;
    });
```

The test consumes that spy in the same way it did earlier.

```
it('#getValue should return stubbed value from a spy', () => {
      const stubValue = 'stub value';
      valueServiceSpy.getValue.and.returnValue(stubValue);

      expect(masterService.getValue()).withContext('service returned stub value').toBe(stubValue);
      expect(valueServiceSpy.getValue.calls.count())
        .withContext('spy method was called once')
        .toBe(1);
      expect(valueServiceSpy.getValue.calls.mostRecent().returnValue).toBe(stubValue);
    });
```

## Testing without beforeEach()

Most test suites in this guide call `beforeEach()` to set the preconditions for each `it()` test and rely on the [`TestBed`](../../api/core/testing/testbed) to create classes and inject services.

There's another school of testing that never calls `beforeEach()` and prefers to create classes explicitly rather than use the [`TestBed`](../../api/core/testing/testbed).

Here's how you might rewrite one of the `MasterService` tests in that style.

Begin by putting re-usable, preparatory code in a *setup* function instead of `beforeEach()`.

```
function setup() {
      const valueServiceSpy = jasmine.createSpyObj('ValueService', ['getValue']);
      const stubValue = 'stub value';
      const masterService = new MasterService(valueServiceSpy);

      valueServiceSpy.getValue.and.returnValue(stubValue);
      return {masterService, stubValue, valueServiceSpy};
    }
```

The `setup()` function returns an object literal with the variables, such as `masterService`, that a test might reference. You don't define *semi-global* variables (for example, `let masterService: MasterService`) in the body of the `describe()`.

Then each test invokes `setup()` in its first line, before continuing with steps that manipulate the test subject and assert expectations.

```
it('#getValue should return stubbed value from a spy', () => {
      const {masterService, stubValue, valueServiceSpy} = setup();
      expect(masterService.getValue()).withContext('service returned stub value').toBe(stubValue);
      expect(valueServiceSpy.getValue.calls.count())
        .withContext('spy method was called once')
        .toBe(1);
      expect(valueServiceSpy.getValue.calls.mostRecent().returnValue).toBe(stubValue);
    });
```

Notice how the test uses [*destructuring assignment*](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to extract the setup variables that it needs.

```
const {masterService, stubValue, valueServiceSpy} = setup();
```

Many developers feel this approach is cleaner and more explicit than the traditional `beforeEach()` style.

Although this testing guide follows the traditional style and the default [CLI schematics](https://github.com/angular/angular-cli) generate test files with `beforeEach()` and [`TestBed`](../../api/core/testing/testbed), feel free to adopt *this alternative approach* in your own projects.

## Testing HTTP services

Data services that make HTTP calls to remote servers typically inject and delegate to the Angular [`HttpClient`](../../api/common/http/httpclient) service for XHR calls.

You can test a data service with an injected [`HttpClient`](../../api/common/http/httpclient) spy as you would test any service with a dependency.

```
let httpClientSpy: jasmine.SpyObj<HttpClient>;
  let heroService: HeroService;

  beforeEach(() => {
    // TODO: spy on other methods too
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get']);
    heroService = new HeroService(httpClientSpy);
  });

  it('should return expected heroes (HttpClient called once)', (done: DoneFn) => {
    const expectedHeroes: Hero[] = [
      {id: 1, name: 'A'},
      {id: 2, name: 'B'},
    ];

    httpClientSpy.get.and.returnValue(asyncData(expectedHeroes));

    heroService.getHeroes().subscribe({
      next: (heroes) => {
        expect(heroes).withContext('expected heroes').toEqual(expectedHeroes);
        done();
      },
      error: done.fail,
    });
    expect(httpClientSpy.get.calls.count()).withContext('one call').toBe(1);
  });

  it('should return an error when the server returns a 404', (done: DoneFn) => {
    const errorResponse = new HttpErrorResponse({
      error: 'test 404 error',
      status: 404,
      statusText: 'Not Found',
    });

    httpClientSpy.get.and.returnValue(asyncError(errorResponse));

    heroService.getHeroes().subscribe({
      next: (heroes) => done.fail('expected an error, not heroes'),
      error: (error) => {
        expect(error.message).toContain('test 404 error');
        done();
      },
    });
  });
```

**IMPORTANT:** The `HeroService` methods return `Observables`. You must *subscribe* to an observable to (a) cause it to execute and (b) assert that the method succeeds or fails.

The `subscribe()` method takes a success (`next`) and fail (`error`) callback. Make sure you provide *both* callbacks so that you capture errors. Neglecting to do so produces an asynchronous uncaught observable error that the test runner will likely attribute to a completely different test.

## HttpClientTestingModule

Extended interactions between a data service and the [`HttpClient`](../../api/common/http/httpclient) can be complex and difficult to mock with spies.

The [`HttpClientTestingModule`](../../api/common/http/testing/httpclienttestingmodule) can make these testing scenarios more manageable.

While the *code sample* accompanying this guide demonstrates [`HttpClientTestingModule`](../../api/common/http/testing/httpclienttestingmodule), this page defers to the [Http guide](../http/testing), which covers testing with the [`HttpClientTestingModule`](../../api/common/http/testing/httpclienttestingmodule) in detail.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/testing/services>
