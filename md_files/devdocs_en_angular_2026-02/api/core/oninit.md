# OnInit

OnInit



# OnInit

A lifecycle hook that is called after Angular has initialized all data-bound properties of a directive. Define an `ngOnInit()` method to handle any additional initialization tasks.

[AfterContentInit](aftercontentinit)[Lifecycle hooks guide](../../guide/components/lifecycle)

## API

```
interface OnInit {
  ngOnInit(): void;
}
```

### ngOnInit

`void`

A callback method that is invoked immediately after the default change detector has checked the directive's data-bound properties for the first time, and before any of the view or content children have been checked. It is invoked only once when the directive is instantiated.

@returns`void`

## Usage Notes

The following snippet shows how a component can implement this interface to define its own initialization method.

```
@Component({
        selector: 'my-cmp',
        template: `...`,
        standalone: false,
      })
      class MyComponent implements OnInit {
        ngOnInit() {
          // ...
        }
      }
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/OnInit>
