# RouterLink

RouterLink



# RouterLink

When applied to an element in a template, makes that element a link that initiates navigation to a route. Navigation opens one or more routed components in one or more `<router-outlet>` locations on the page.

## API

```
class RouterLink implements OnChanges ,OnDestroy {
  constructor(router: Router, route: ActivatedRoute, tabIndexAttribute: string | null | undefined, renderer: Renderer2, el: ElementRef<any>, locationStrategy?: LocationStrategy | undefined): RouterLink;
  protected readonly reactiveHref: WritableSignal<string | null>;
   get href(): string | null;
  @Input() target?: string | undefined;
  @Input() queryParams?: Params | null | undefined;
  @Input() fragment?: string | undefined;
  @Input() queryParamsHandling?: QueryParamsHandling | null | undefined;
  @Input() state?: { [k: string]: any; } | undefined;
  @Input() info?: unknown;
  @Input() relativeTo?: ActivatedRoute | null | undefined;
  @Input() preserveFragment: boolean;
  @Input() skipLocationChange: boolean;
  @Input() replaceUrl: boolean;
  @Input() set routerLink(value: string | readonly any[] | UrlTree | null | undefined);
  readonly urlTree: UrlTree | null;
}
```

### constructor

`RouterLink`

@paramrouter`Router`

@paramroute`ActivatedRoute`

@paramtabIndexAttribute`string | null | undefined`

@paramrenderer`Renderer2`

@paramel`ElementRef<any>`

@paramlocationStrategy`LocationStrategy | undefined`

@returns`RouterLink`

### reactiveHref

`WritableSignal<string | null>`

### href

`string | null`

Represents an `href` attribute value applied to a host element, when a host element is an `<a>`/`<area>` tag or a compatible custom element. For other tags, the value is `null`.

### href

`string | null`

### target

`string | undefined`

Represents the `target` attribute on a host element. This is only used when the host element is an `<a>`/`<area>` tag or a compatible custom element.

### queryParams

`Params | null | undefined`

Passed to [`Router#createUrlTree`](router#createUrlTree) as part of the [`UrlCreationOptions`](urlcreationoptions).

### fragment

`string | undefined`

Passed to [`Router#createUrlTree`](router#createUrlTree) as part of the [`UrlCreationOptions`](urlcreationoptions).

### queryParamsHandling

`QueryParamsHandling | null | undefined`

Passed to [`Router#createUrlTree`](router#createUrlTree) as part of the [`UrlCreationOptions`](urlcreationoptions).

### state

`{ [k: string]: any; } | undefined`

Passed to [`Router#navigateByUrl`](router#navigateByUrl) as part of the [`NavigationBehaviorOptions`](navigationbehavioroptions).

### info

`unknown`

Passed to [`Router#navigateByUrl`](router#navigateByUrl) as part of the [`NavigationBehaviorOptions`](navigationbehavioroptions).

### relativeTo

`ActivatedRoute | null | undefined`

Passed to [`Router#createUrlTree`](router#createUrlTree) as part of the [`UrlCreationOptions`](urlcreationoptions). Specify a value here when you do not want to use the default value for `routerLink`, which is the current activated route. Note that a value of `undefined` here will use the `routerLink` default.

### preserveFragment

`boolean`

Passed to [`Router#createUrlTree`](router#createUrlTree) as part of the [`UrlCreationOptions`](urlcreationoptions).

### skipLocationChange

`boolean`

Passed to [`Router#navigateByUrl`](router#navigateByUrl) as part of the [`NavigationBehaviorOptions`](navigationbehavioroptions).

### replaceUrl

`boolean`

Passed to [`Router#navigateByUrl`](router#navigateByUrl) as part of the [`NavigationBehaviorOptions`](navigationbehavioroptions).

### routerLink

`string | readonly any[] | UrlTree | null | undefined`

Commands to pass to [`Router#createUrlTree`](router#createUrlTree) or a [`UrlTree`](urltree).

- **array**: commands to pass to [`Router#createUrlTree`](router#createUrlTree).
- **string**: shorthand for array of commands with just the string, i.e. `['/route']`
- **UrlTree**: a [`UrlTree`](urltree) for this link rather than creating one from the commands and other inputs that correspond to properties of [`UrlCreationOptions`](urlcreationoptions).
- **null|undefined**: effectively disables the `routerLink`

### urlTree

`UrlTree | null`

## Description

When applied to an element in a template, makes that element a link that initiates navigation to a route. Navigation opens one or more routed components in one or more `<router-outlet>` locations on the page.

Given a route configuration `[{ path: 'user/:name', component: UserCmp }]`, the following creates a static link to the route: `<a routerLink="/user/bob">link to user component</a>`

You can use dynamic values to generate the link. For a dynamic link, pass an array of path segments, followed by the params for each segment. For example, `['/team', teamId, 'user', userName, {details: true}]` generates a link to `/team/11/user/bob;details=true`.

Multiple static segments can be merged into one term and combined with dynamic segments. For example, `['/team/11/user', userName, {details: true}]`

The input that you provide to the link is treated as a delta to the current URL. For instance, suppose the current URL is `/user/(box//aux:team)`. The link `<a [routerLink]="['/user/jim']">Jim</a>` creates the URL `/user/(jim//aux:team)`. See [`Router#createUrlTree`](router#createUrlTree) for more information.

---

## Exported by

- `RouterModule`

## Usage Notes

You can use absolute or relative paths in a link, set query parameters, control how parameters are handled, and keep a history of navigation states.

### Relative link paths

The first segment name can be prepended with `/`, `./`, or `../`.

- If the first segment begins with `/`, the router looks up the route from the root of the app.
- If the first segment begins with `./`, or doesn't begin with a slash, the router looks in the children of the current activated route.
- If the first segment begins with `../`, the router goes up one level in the route tree.

### Setting and handling query params and fragments

The following link adds a query parameter and a fragment to the generated URL:

```
<a [routerLink]="['/user/bob']" [queryParams]="{debug: true}" fragment="education">
  link to user component
</a>
```

By default, the directive constructs the new URL using the given query parameters. The example generates the link: `/user/bob?debug=true#education`.

You can instruct the directive to handle query parameters differently by specifying the `queryParamsHandling` option in the link. Allowed values are:

- `'merge'`: Merge the given `queryParams` into the current query params.
- `'preserve'`: Preserve the current query params.

For example:

```
<a [routerLink]="['/user/bob']" [queryParams]="{debug: true}" queryParamsHandling="merge">
  link to user component
</a>
```

`queryParams`, `fragment`, `queryParamsHandling`, `preserveFragment`, and `relativeTo` cannot be used when the `routerLink` input is a [`UrlTree`](urltree).

See [`UrlCreationOptions#queryParamsHandling`](urlcreationoptions#queryParamsHandling).

### Preserving navigation history

You can provide a `state` value to be persisted to the browser's [`History.state` property](https://developer.mozilla.org/en-US/docs/Web/API/History#Properties). For example:

```
<a [routerLink]="['/user/bob']" [state]="{tracingId: 123}">
  link to user component
</a>
```

Use [`Router#getCurrentNavigation`](router#getCurrentNavigation) to retrieve a saved navigation-state value. For example, to capture the `tracingId` during the [`NavigationStart`](navigationstart) event:

```
// Get NavigationStart events
router.events.pipe(filter(e => e instanceof NavigationStart)).subscribe(e => {
  const navigation = router.getCurrentNavigation();
  tracingService.trace({id: navigation.extras.state.tracingId});
});
```

### RouterLink compatible custom elements

In order to make a custom element work with routerLink, the corresponding custom element must implement the `href` attribute and must list `href` in the array of the static property/getter `observedAttributes`.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterLink>
