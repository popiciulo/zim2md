# OnChanges

OnChanges



# OnChanges

A lifecycle hook that is called when any data-bound property of a directive changes. Define an `ngOnChanges()` method to handle the changes.

[DoCheck](docheck)[OnInit](oninit)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface OnChanges {
  ngOnChanges(changes: { [propName: string]: SimpleChange<any>; }): void;
}
```

### ngOnChanges

`void`

A callback method that is invoked immediately after the default change detector has checked data-bound properties if at least one has changed, and before the view and content children are checked.

@paramchanges`{ [propName: string]: SimpleChange<any>; }`

The changed properties.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define an on-changes handler for an input property.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements OnChanges {
        @Input() prop: number = 0;

        ngOnChanges(changes: SimpleChanges) {
          // changes.prop contains the old and the new value...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OnChanges>
