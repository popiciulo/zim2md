# UrlCreationOptions

UrlCreationOptions



# UrlCreationOptions

Options that modify the [`Router`](router) URL. Supply an object containing any of these properties to a [`Router`](router) navigation function to control how the target URL should be constructed.

[Router#navigate](router#navigate)[Router#createUrlTree](router#createUrlTree)[Routing and Navigation guide](../../guide/routing/common-router-tasks)

## API

```
interface UrlCreationOptions {
  relativeTo?: ActivatedRoute | null | undefined;
  queryParams?: Params | null | undefined;
  fragment?: string | undefined;
  queryParamsHandling?: QueryParamsHandling | null | undefined;
  preserveFragment?: boolean | undefined;
}
```

### relativeTo

`ActivatedRoute | null | undefined`

Specifies a root URI to use for relative navigation.

For example, consider the following route configuration where the parent route has two children.

```
[{
  path: 'parent',
  component: ParentComponent,
  children: [{
    path: 'list',
    component: ListComponent
  },{
    path: 'child',
    component: ChildComponent
  }]
}]
```

The following `go()` function navigates to the `list` route by interpreting the destination URI as relative to the activated `child` route

```
 @Component({...})
 class ChildComponent {
   constructor(private router: Router, private route: ActivatedRoute) {}

   go() {
     router.navigate(['../list'], { relativeTo: this.route });
   }
 }
```

A value of `null` or `undefined` indicates that the navigation commands should be applied relative to the root.

### queryParams

`Params | null | undefined`

Sets query parameters to the URL.

```
// Navigate to /results?page=1
router.navigate(['/results'], { queryParams: { page: 1 } });
```

### fragment

`string | undefined`

Sets the hash fragment for the URL.

```
// Navigate to /results#top
router.navigate(['/results'], { fragment: 'top' });
```

### queryParamsHandling

`QueryParamsHandling | null | undefined`

How to handle query parameters in the router link for the next navigation. One of:

- `preserve` : Preserve current parameters.
- `merge` : Merge new with current parameters.

The "preserve" option discards any new query params:

```
// from /view1?page=1 to/view2?page=1
router.navigate(['/view2'], { queryParams: { page: 2 },  queryParamsHandling: "preserve"
});
```

The "merge" option appends new query params to the params from the current URL:

```
// from /view1?page=1 to/view2?page=1&otherKey=2
router.navigate(['/view2'], { queryParams: { otherKey: 2 },  queryParamsHandling: "merge"
});
```

In case of a key collision between current parameters and those in the `queryParams` object, the new value is used.

### preserveFragment

`boolean | undefined`

When true, preserves the URL fragment for the next navigation

```
// Preserve fragment from /results#top to /view#top
router.navigate(['/view'], { preserveFragment: true });
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/UrlCreationOptions>
