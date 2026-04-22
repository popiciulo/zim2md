# RouterTestingHarness

RouterTestingHarness



# RouterTestingHarness

A testing harness for the `Router` to reduce the boilerplate needed to test routes and routed components.

## API

```
class RouterTestingHarness {
  constructor(fixture: ComponentFixture<{ routerOutletData: WritableSignal<unknown>; }>): RouterTestingHarness;
  readonly fixture: ComponentFixture<{ routerOutletData: WritableSignal<unknown>; }>;
  detectChanges(): void;
  readonly routeDebugElement: DebugElement | null;
  readonly routeNativeElement: HTMLElement | null;
  navigateByUrl(url: string): Promise<{} | null>;
  navigateByUrl<T>(url: string, requiredRoutedComponentType: Type<T>): Promise<T>;
  static create(initialUrl?: string | undefined): Promise<RouterTestingHarness>;
}
```

### constructor

`RouterTestingHarness`

@paramfixture`ComponentFixture<{ routerOutletData: WritableSignal<unknown>; }>`

@returns`RouterTestingHarness`

### fixture

`ComponentFixture<{ routerOutletData: WritableSignal<unknown>; }>`

Fixture of the root component of the RouterTestingHarness

### detectChanges

`void`

Instructs the root fixture to run change detection.

@returns`void`

### routeDebugElement

`DebugElement | null`

The [`DebugElement`](../../core/debugelement) of the `RouterOutlet` component. `null` if the outlet is not activated.

### routeNativeElement

`HTMLElement | null`

The native element of the `RouterOutlet` component. `null` if the outlet is not activated.

### navigateByUrl

2 overloads

Triggers a `Router` navigation and waits for it to complete.

The root component with a `RouterOutlet` created for the harness is used to render `Route` components. The root component is reused within the same test in subsequent calls to `navigateForTest`.

When testing `Routes` with a guards that reject the navigation, the `RouterOutlet` might not be activated and the `activatedComponent` may be `null`.

```
let isLoggedIn = false;
    const isLoggedInGuard: CanActivateFn = () => {
      return isLoggedIn ? true : inject(Router).parseUrl('/login');
    };

    TestBed.configureTestingModule({
      providers: [
        provideRouter([
          {path: 'admin', canActivate: [isLoggedInGuard], component: AdminComponent},
          {path: 'login', component: LoginComponent},
        ]),
      ],
    });

    const harness = await RouterTestingHarness.create('/admin');
    expect(TestBed.inject(Router).url).toEqual('/login');
    isLoggedIn = true;
    await harness.navigateByUrl('/admin');
    expect(TestBed.inject(Router).url).toEqual('/admin');
```

@paramurl`string`

The target of the navigation. Passed to `Router.navigateByUrl`.

@returns`Promise<{} | null>`

Triggers a router navigation and waits for it to complete.

The root component with a `RouterOutlet` created for the harness is used to render `Route` components.

```
it('navigates to routed component', async () => {
    @Component({standalone: true, template: 'hello {{name}}'})
    class TestCmp {
      name = 'world';
    }

    TestBed.configureTestingModule({
      providers: [provideRouter([{path: '', component: TestCmp}])],
    });

    const harness = await RouterTestingHarness.create();
    const activatedComponent = await harness.navigateByUrl('/', TestCmp);
    expect(activatedComponent).toBeInstanceOf(TestCmp);
    expect(harness.routeNativeElement?.innerHTML).toContain('hello world');
  });
```

The root component is reused within the same test in subsequent calls to `navigateByUrl`.

This function also makes it easier to test components that depend on `ActivatedRoute` data.

```
@Component({
      imports: [AsyncPipe],
      template: `search: {{ (route.queryParams | async)?.query }}`,
    })
    class SearchCmp {
      constructor(
        readonly route: ActivatedRoute,
        readonly router: Router,
      ) {}

      async searchFor(thing: string) {
        await this.router.navigate([], {queryParams: {query: thing}});
      }
    }

    TestBed.configureTestingModule({
      providers: [provideRouter([{path: 'search', component: SearchCmp}])],
    });

    const harness = await RouterTestingHarness.create();
    const activatedComponent = await harness.navigateByUrl('/search', SearchCmp);
    await activatedComponent.searchFor('books');
    harness.detectChanges();
    expect(TestBed.inject(Router).url).toEqual('/search?query=books');
    expect(harness.routeNativeElement?.innerHTML).toContain('books');
```

@paramurl`string`

The target of the navigation. Passed to `Router.navigateByUrl`.

@paramrequiredRoutedComponentType`Type<T>`

After navigation completes, the required type for the activated component of the `RouterOutlet`. If the outlet is not activated or a different component is activated, this function will throw an error.

@returns`Promise<T>`

### create

`Promise<RouterTestingHarness>`

Creates a [`RouterTestingHarness`](routertestingharness) instance.

The [`RouterTestingHarness`](routertestingharness) also creates its own root component with a `RouterOutlet` for the purposes of rendering route components.

Throws an error if an instance has already been created. Use of this harness also requires `destroyAfterEach: true` in the `ModuleTeardownOptions`

@paraminitialUrl`string | undefined`

The target of navigation to trigger before returning the harness.

@returns`Promise<RouterTestingHarness>`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/testing/RouterTestingHarness>
