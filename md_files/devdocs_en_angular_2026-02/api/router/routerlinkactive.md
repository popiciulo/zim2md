# RouterLinkActive

RouterLinkActive



# RouterLinkActive

Tracks whether the linked route of an element is currently active, and allows you to specify one or more CSS classes to add to the element when the linked route is active.

[Detect active current route with RouterLinkActive](../../guide/routing/read-route-state#detect-active-current-route-with-routerlinkactive)

## API

```
class RouterLinkActive implements OnChanges ,OnDestroy ,AfterContentInit {
  constructor(router: Router, element: ElementRef<any>, renderer: Renderer2, cdr: ChangeDetectorRef): RouterLinkActive;
  links: QueryList<RouterLink>;
  readonly isActive: boolean;
  @Input() routerLinkActiveOptions: IsActiveMatchOptions | { exact: boolean; };
  @Input() ariaCurrentWhenActive?: boolean | "page" | "step" | "location" | "date" | "time" | undefined;
  readonly @Output() isActiveChange: EventEmitter<boolean>;
  @Input() set routerLinkActive(value: string | string[]);
}
```

### constructor

`RouterLinkActive`

@paramrouter`Router`

@paramelement`ElementRef<any>`

@paramrenderer`Renderer2`

@paramcdr`ChangeDetectorRef`

@returns`RouterLinkActive`

### links

`QueryList<RouterLink>`

### isActive

`boolean`

### routerLinkActiveOptions

`IsActiveMatchOptions | { exact: boolean; }`

Options to configure how to determine if the router link is active.

These options are passed to the [`Router.isActive()`](router#isActive) function.

### ariaCurrentWhenActive

`boolean | "page" | "step" | "location" | "date" | "time" | undefined`

Aria-current attribute to apply when the router link is active.

Possible values: `'page'` | `'step'` | `'location'` | `'date'` | `'time'` | `true` | `false`.

### isActiveChange

`EventEmitter<boolean>`

You can use the output `isActiveChange` to get notified each time the link becomes active or inactive.

Emits: true -> Route is active false -> Route is inactive

```
<a
 routerLink="/user/bob"
 routerLinkActive="active-link"
 (isActiveChange)="this.onRouterLinkActive($event)">Bob</a>
```

### routerLinkActive

`string | string[]`

## Description

Tracks whether the linked route of an element is currently active, and allows you to specify one or more CSS classes to add to the element when the linked route is active.

Use this directive to create a visual distinction for elements associated with an active route. For example, the following code highlights the word "Bob" when the router activates the associated route:

```
<a routerLink="/user/bob" routerLinkActive="active-link">Bob</a>
```

Whenever the URL is either '/user' or '/user/bob', the "active-link" class is added to the anchor tag. If the URL changes, the class is removed.

You can set more than one class using a space-separated string or an array. For example:

```
<a routerLink="/user/bob" routerLinkActive="class1 class2">Bob</a>
<a routerLink="/user/bob" [routerLinkActive]="['class1', 'class2']">Bob</a>
```

To add the classes only when the URL matches the link exactly, add the option `exact: true`:

```
<a routerLink="/user/bob" routerLinkActive="active-link" [routerLinkActiveOptions]="{exact:
true}">Bob</a>
```

To directly check the `isActive` status of the link, assign the [`RouterLinkActive`](routerlinkactive) instance to a template variable. For example, the following checks the status without assigning any CSS classes:

```
<a routerLink="/user/bob" routerLinkActive #rla="routerLinkActive">
  Bob {{ rla.isActive ? '(already open)' : ''}}
</a>
```

You can apply the [`RouterLinkActive`](routerlinkactive) directive to an ancestor of linked elements. For example, the following sets the active-link class on the `<div>` parent tag when the URL is either '/user/jim' or '/user/bob'.

```
<div routerLinkActive="active-link" [routerLinkActiveOptions]="{exact: true}">
  <a routerLink="/user/jim">Jim</a>
  <a routerLink="/user/bob">Bob</a>
</div>
```

The [`RouterLinkActive`](routerlinkactive) directive can also be used to set the aria-current attribute to provide an alternative distinction for active elements to visually impaired users.

For example, the following code adds the 'active' class to the Home Page link when it is indeed active and in such case also sets its aria-current attribute to 'page':

```
<a routerLink="/" routerLinkActive="active" ariaCurrentWhenActive="page">Home Page</a>
```

**NOTE:** RouterLinkActive is a [`ContentChildren`](../core/contentchildren) query. Content children queries do not retrieve elements or directives that are in other components' templates, since a component's template is always a black box to its ancestors.

---

## Exported by

- `RouterModule`

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/RouterLinkActive>
