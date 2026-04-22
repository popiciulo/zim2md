# reflectComponentType

reflectComponentType



# reflectComponentType

Creates an object that allows to retrieve component metadata.

## API

```
function reflectComponentType<C>(component: Type<C>): ComponentMirror<C> | null;
```

### reflectComponentType

`ComponentMirror<C> | null`

Creates an object that allows to retrieve component metadata.

@paramcomponent`Type<C>`

Component class reference.

@returns`ComponentMirror<C> | null`

Usage notes

The example below demonstrates how to use the function and how the fields of the returned object map to the component metadata.

```
@Component({
  selector: 'foo-component',
  template: `
    <ng-content></ng-content>
    <ng-content select="content-selector-a"></ng-content>
  `,
})
class FooComponent {
  @Input('inputName') inputPropName: string;
  @Output('outputName') outputPropName = new EventEmitter<void>();
}

const mirror = reflectComponentType(FooComponent);
expect(mirror.type).toBe(FooComponent);
expect(mirror.selector).toBe('foo-component');
expect(mirror.isStandalone).toBe(true);
expect(mirror.inputs).toEqual([{propName: 'inputName', templateName: 'inputPropName'}]);
expect(mirror.outputs).toEqual([{propName: 'outputName', templateName: 'outputPropName'}]);
expect(mirror.ngContentSelectors).toEqual([
  '*',                 // first `<ng-content>` in a template, the selector defaults to `*`
  'content-selector-a' // second `<ng-content>` in a template
]);
```

## Usage Notes

The example below demonstrates how to use the function and how the fields of the returned object map to the component metadata.

```
@Component({
  selector: 'foo-component',
  template: `
    <ng-content></ng-content>
    <ng-content select="content-selector-a"></ng-content>
  `,
})
class FooComponent {
  @Input('inputName') inputPropName: string;
  @Output('outputName') outputPropName = new EventEmitter<void>();
}

const mirror = reflectComponentType(FooComponent);
expect(mirror.type).toBe(FooComponent);
expect(mirror.selector).toBe('foo-component');
expect(mirror.isStandalone).toBe(true);
expect(mirror.inputs).toEqual([{propName: 'inputName', templateName: 'inputPropName'}]);
expect(mirror.outputs).toEqual([{propName: 'outputName', templateName: 'outputPropName'}]);
expect(mirror.ngContentSelectors).toEqual([
  '*',                 // first `<ng-content>` in a template, the selector defaults to `*`
  'content-selector-a' // second `<ng-content>` in a template
]);
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/reflectComponentType>
