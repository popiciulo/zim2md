# InMemoryScrollingOptions

InMemoryScrollingOptions



# InMemoryScrollingOptions

Configuration options for the scrolling feature which can be used with [`withInMemoryScrolling`](withinmemoryscrolling) function.

## API

```
interface InMemoryScrollingOptions {
  anchorScrolling?: "disabled" | "enabled" | undefined;
  scrollPositionRestoration?: "disabled" | "enabled" | "top" | undefined;
}
```

### anchorScrolling

`"disabled" | "enabled" | undefined`

When set to 'enabled', scrolls to the anchor element when the URL has a fragment. Anchor scrolling is disabled by default.

Anchor scrolling does not happen on 'popstate'. Instead, we restore the position that we stored or scroll to the top.

### scrollPositionRestoration

`"disabled" | "enabled" | "top" | undefined`

Configures if the scroll position needs to be restored when navigating back.

- 'disabled'- (Default) Does nothing. Scroll position is maintained on navigation.
- 'top'- Sets the scroll position to x = 0, y = 0 on all navigation.
- 'enabled'- Restores the previous scroll position on backward navigation, else sets the position to the anchor if one is provided, or sets the scroll position to [0, 0] (forward navigation). This option will be the default in the future.

You can implement custom scroll restoration behavior by adapting the enabled behavior as in the following example.

```
class AppComponent {
  movieData: any;

  constructor(private router: Router, private viewportScroller: ViewportScroller,
changeDetectorRef: ChangeDetectorRef) {
  router.events.pipe(filter((event: Event): event is Scroll => event instanceof Scroll)
    ).subscribe(e => {
      fetch('http://example.com/movies.json').then(response => {
        this.movieData = response.json();
        // update the template with the data before restoring scroll
        changeDetectorRef.detectChanges();

        if (e.position) {
          viewportScroller.scrollToPosition(e.position);
        }
      });
    });
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/router/InMemoryScrollingOptions>
