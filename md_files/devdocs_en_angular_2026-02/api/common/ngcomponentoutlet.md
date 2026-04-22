# NgComponentOutlet

NgComponentOutlet



# NgComponentOutlet

Instantiates a [`Component`](../core/component) type and inserts its Host View into the current View. [`NgComponentOutlet`](ngcomponentoutlet) provides a declarative approach for dynamic component creation.

## API

```
class NgComponentOutlet<T = any> implements OnChanges ,DoCheck ,OnDestroy {
  constructor(_viewContainerRef: ViewContainerRef): NgComponentOutlet<T>;
  @Input() ngComponentOutlet: Type<T> | null;
  @Input() ngComponentOutletInputs?: Record<string, unknown> | undefined;
  @Input() ngComponentOutletInjector?: Injector | undefined;
  @Input() ngComponentOutletEnvironmentInjector?: EnvironmentInjector | undefined;
  @Input() ngComponentOutletContent?: Node[][] | undefined;
  @Input() ngComponentOutletNgModule?: Type<any> | undefined;
  readonly componentInstance: T | null;
}
```

### constructor

`NgComponentOutlet<T>`

@param\_viewContainerRef`ViewContainerRef`

@returns`NgComponentOutlet<T>`

### ngComponentOutlet

`Type<T> | null`

Component that should be rendered in the outlet.

### ngComponentOutletInputs

`Record<string, unknown> | undefined`

### ngComponentOutletInjector

`Injector | undefined`

### ngComponentOutletEnvironmentInjector

`EnvironmentInjector | undefined`

### ngComponentOutletContent

`Node[][] | undefined`

### ngComponentOutletNgModule

`Type<any> | undefined`

### componentInstance

`T | null`

Gets the instance of the currently-rendered component. Will be null if no component has been rendered.

## Description

Instantiates a [`Component`](../core/component) type and inserts its Host View into the current View. [`NgComponentOutlet`](ngcomponentoutlet) provides a declarative approach for dynamic component creation.

[`NgComponentOutlet`](ngcomponentoutlet) requires a component type, if a falsy value is set the view will clear and any existing component will be destroyed.

---

## Exported by

- `CommonModule`

## Usage Notes

### Fine tune control

You can control the component creation process by using the following optional attributes:

- `ngComponentOutletInputs`: Optional component inputs object, which will be bind to the component.
- `ngComponentOutletInjector`: Optional custom [`Injector`](../core/injector) that will be used as parent for the Component. Defaults to the injector of the current view container.
- `ngComponentOutletEnvironmentInjector`: Optional custom [`EnvironmentInjector`](../core/environmentinjector) which will provide the component's environment.
- `ngComponentOutletContent`: Optional list of projectable nodes to insert into the content section of the component, if it exists.
- `ngComponentOutletNgModule`: Optional NgModule class reference to allow loading another module dynamically, then loading a component from that module.

### Syntax

Simple

```
<ng-container *ngComponentOutlet="componentTypeExpression"></ng-container>
```

With inputs

```
<ng-container *ngComponentOutlet="componentTypeExpression;
                                  inputs: inputsExpression;">
</ng-container>
```

Customized injector/content

```
<ng-container *ngComponentOutlet="componentTypeExpression;
                                  injector: injectorExpression;
                                  content: contentNodesExpression;">
</ng-container>
```

Customized NgModule reference

```
<ng-container *ngComponentOutlet="componentTypeExpression;
                                  ngModule: ngModuleClass;">
</ng-container>
```

### A simple example

```
@Component({
  selector: 'hello-world',
  template: 'Hello World!',
})
export class HelloWorld {}

@Component({
  selector: 'ng-component-outlet-simple-example',
  imports: [NgComponentOutlet],
  template: `<ng-container *ngComponentOutlet="HelloWorld"></ng-container>`,
})
export class NgComponentOutletSimpleExample {
  // This field is necessary to expose HelloWorld to the template.
  HelloWorld = HelloWorld;
}
```

A more complete example with additional options:

```
@Injectable()
export class Greeter {
  suffix = '!';
}

@Component({
  selector: 'complete-component',
  template: `{{ label() }}: <ng-content></ng-content> <ng-content></ng-content>{{ greeter.suffix }}`,
})
export class CompleteComponent {
  label = input.required<string>();

  constructor(public greeter: Greeter) {}
}

@Component({
  selector: 'ng-component-outlet-complete-example',
  imports: [NgComponentOutlet],
  template: ` <ng-template #ahoj>Ahoj</ng-template>
    <ng-template #svet>Svet</ng-template>
    <ng-container
      *ngComponentOutlet="
        CompleteComponent;
        inputs: myInputs;
        injector: myInjector;
        content: myContent
      "
    ></ng-container>`,
})
export class NgComponentOutletCompleteExample {
  // This field is necessary to expose CompleteComponent to the template.
  CompleteComponent = CompleteComponent;

  myInputs = {'label': 'Complete'};

  myInjector: Injector;
  ahojTemplateRef = viewChild.required<TemplateRef<any>>('ahoj');
  svetTemplateRef = viewChild.required<TemplateRef<any>>('svet');
  myContent?: any[][];

  constructor(
    injector: Injector,
    private vcr: ViewContainerRef,
  ) {
    this.myInjector = Injector.create({
      providers: [{provide: Greeter, deps: []}],
      parent: injector,
    });

    effect(() => {
      this.myContent = [
        this.vcr.createEmbeddedView(this.ahojTemplateRef()).rootNodes,
        this.vcr.createEmbeddedView(this.svetTemplateRef()).rootNodes,
      ];
    });
  }
}
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/NgComponentOutlet>
