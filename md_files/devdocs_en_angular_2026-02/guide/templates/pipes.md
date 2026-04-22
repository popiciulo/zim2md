# Pipes

Pipes



# Pipes

  

## Overview

Pipes are a special operator in Angular template expressions that allows you to transform data declaratively in your template. Pipes let you declare a transformation function once and then use that transformation across multiple templates. Angular pipes use the vertical bar character (`|`), inspired by the [Unix pipe](https://en.wikipedia.org/wiki/Pipeline_(Unix)).

**NOTE:** Angular's pipe syntax deviates from standard JavaScript, which uses the vertical bar character for the [bitwise OR operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_OR). Angular template expressions do not support bitwise operators.

Here is an example using some built-in pipes that Angular provides:

```
import { Component } from '@angular/core';
import { CurrencyPipe, DatePipe, TitleCasePipe } from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [CurrencyPipe, DatePipe, TitleCasePipe],
  template: `
    <main>
       <!-- Transform the company name to title-case and
       transform the purchasedOn date to a locale-formatted string -->
<h1>Purchases from {{ company | titlecase }} on {{ purchasedOn | date }}</h1>

	    <!-- Transform the amount to a currency-formatted string -->
      <p>Total: {{ amount | currency }}</p>
    </main>
  `,
})
export class ShoppingCartComponent {
  amount = 123.45;
  company = 'acme corporation';
  purchasedOn = '2024-07-08';
}
```

When Angular renders the component, it will ensure that the appropriate date format and currency is based on the locale of the user. If the user is in the United States, it would render:

```
<main>
  <h1>Purchases from Acme Corporation on Jul 8, 2024</h1>
  <p>Total: $123.45</p>
</main>
```

See the [in-depth guide on i18n](../i18n) to learn more about how Angular localizes values.

### Built-in Pipes

Angular includes a set of built-in pipes in the `@angular/common` package:

| Name | Description |
| --- | --- |
| [`AsyncPipe`](../../api/common/asyncpipe) | Read the value from a `Promise` or an RxJS `Observable`. |
| [`CurrencyPipe`](../../api/common/currencypipe) | Transforms a number to a currency string, formatted according to locale rules. |
| [`DatePipe`](../../api/common/datepipe) | Formats a `Date` value according to locale rules. |
| [`DecimalPipe`](../../api/common/decimalpipe) | Transforms a number into a string with a decimal point, formatted according to locale rules. |
| [`I18nPluralPipe`](../../api/common/i18npluralpipe) | Maps a value to a string that pluralizes the value according to locale rules. |
| [`I18nSelectPipe`](../../api/common/i18nselectpipe) | Maps a key to a custom selector that returns a desired value. |
| [`JsonPipe`](../../api/common/jsonpipe) | Transforms an object to a string representation via `JSON.stringify`, intended for debugging. |
| [`KeyValuePipe`](../../api/common/keyvaluepipe) | Transforms Object or Map into an array of key value pairs. |
| [`LowerCasePipe`](../../api/common/lowercasepipe) | Transforms text to all lower case. |
| [`PercentPipe`](../../api/common/percentpipe) | Transforms a number to a percentage string, formatted according to locale rules. |
| [`SlicePipe`](../../api/common/slicepipe) | Creates a new Array or String containing a subset (slice) of the elements. |
| [`TitleCasePipe`](../../api/common/titlecasepipe) | Transforms text to title case. |
| [`UpperCasePipe`](../../api/common/uppercasepipe) | Transforms text to all upper case. |

## Using pipes

Angular's pipe operator uses the vertical bar character (`|`), within a template expression. The pipe operator is a binary operator– the left-hand operand is the value passed to the transformation function, and the right side operand is the name of the pipe and any additional arguments (described below).

```
<p>Total: {{ amount | currency }}</p>
```

In this example, the value of `amount` is passed into the [`CurrencyPipe`](../../api/common/currencypipe) where the pipe name is `currency`. It then renders the default currency for the user’s locale.

### Combining multiple pipes in the same expression

You can apply multiple transformations to a value by using multiple pipe operators. Angular runs the pipes from left to right.

The following example demonstrates a combination of pipes to display a localized date in all uppercase:

```
<p>The event will occur on {{ scheduledOn | date | uppercase }}.</p>
```

### Passing parameters to pipes

Some pipes accept parameters to configure the transformation. To specify a parameter, append the pipe name with a colon (`:`) followed by the parameter value.

For example, the [`DatePipe`](../../api/common/datepipe) is able to take parameters to format the date in a specific way.

```
<p>The event will occur at {{ scheduledOn | date:'hh:mm' }}.</p>
```

Some pipes may accept multiple parameters. You can specify additional parameter values separated by the colon character (`:`).

For example, we can also pass a second optional parameter to control the timezone.

```
<p>The event will occur at {{ scheduledOn | date:'hh:mm':'UTC' }}.</p>
```

## How pipes work

Conceptually, pipes are functions that accept an input value and return a transformed value.

```
import { Component } from '@angular/core';
import { CurrencyPipe} from '@angular/common';

@Component({
  selector: 'app-root',
  imports: [CurrencyPipe],
  template: `
    <main>
      <p>Total: {{ amount | currency }}</p>
    </main>
  `,
})
export class AppComponent {
  amount = 123.45;
}
```

In this example:

1. [`CurrencyPipe`](../../api/common/currencypipe) is imported from `@angular/common`
2. [`CurrencyPipe`](../../api/common/currencypipe) is added to the `imports` array
3. The `amount` data is passed to the `currency` pipe

### Pipe operator precedence

The pipe operator has lower precedence than other binary operators, including `+`, `-`, `*`, `/`, `%`, `&&`, `||`, and `??`.

```
<!-- firstName and lastName are concatenated before the result is passed to the uppercase pipe -->
{{ firstName + lastName | uppercase }}
```

The pipe operator has higher precedence than the conditional (ternary) operator.

```
{{ (isAdmin ? 'Access granted' : 'Access denied') | uppercase }}
```

If the same expression were written without parentheses:

```
{{ isAdmin ? 'Access granted' : 'Access denied' | uppercase }}
```

It will be parsed instead as:

```
{{ isAdmin ? 'Access granted' : ('Access denied' | uppercase) }}
```

Always use parentheses in your expressions when operator precedence may be ambiguous.

### Change detection with pipes

By default, all pipes are considered `pure`, which means that it only executes when a primitive input value (such as a `String`, `Number`, `Boolean`, or `Symbol`) or a object reference (such as `Array`, `Object`, `Function`, or `Date`) is changed. Pure pipes offer a performance advantage because Angular can avoid calling the transformation function if the passed value has not changed.

As a result, this means that mutations to object properties or array items are not detected unless the entire object or array reference is replaced with a different instance. If you want this level of change detection, refer to [detecting changes within arrays or objects](#detecting-change-within-arrays-or-objects).

## Creating custom pipes

You can define a custom pipe by implementing a TypeScript class with the [`@Pipe`](../../api/core/pipe) decorator. A pipe must have two things:

- A name, specified in the pipe decorator
- A method named `transform` that performs the value transformation.

The TypeScript class should additionally implement the [`PipeTransform`](../../api/core/pipetransform) interface to ensure that it satisfies the type signature for a pipe.

Here is an example of a custom pipe that transforms strings to kebab case:

```
// kebab-case.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'kebabCase',
})
export class KebabCasePipe implements PipeTransform {
  transform(value: string): string {
    return value.toLowerCase().replace(/ /g, '-');
  }
}
```

### Using the @Pipe decorator

When creating a custom pipe, import [`Pipe`](../../api/core/pipe) from the `@angular/core` package and use it as a decorator for the TypeScript class.

```
import { Pipe } from '@angular/core';

@Pipe({
  name: 'myCustomTransformation',
})
export class MyCustomTransformationPipe {}
```

The [`@Pipe`](../../api/core/pipe) decorator requires a `name` that controls how the pipe is used in a template.

### Naming convention for custom pipes

The naming convention for custom pipes consists of two conventions:

- `name` - camelCase is recommended. Do not use hyphens.
- `class name` - PascalCase version of the `name` with [`Pipe`](../../api/core/pipe) appended to the end

### Implement the PipeTransform interface

In addition to the [`@Pipe`](../../api/core/pipe) decorator, custom pipes should always implement the [`PipeTransform`](../../api/core/pipetransform) interface from `@angular/core`.

```
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'myCustomTransformation',
})
export class MyCustomTransformationPipe implements PipeTransform {}
```

Implementing this interface ensures that your pipe class has the correct structure.

### Transforming the value of a pipe

Every transformation is invoked by the `transform` method with the first parameter being the value being passed in and the return value being the transformed value.

```
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'myCustomTransformation',
})
export class MyCustomTransformationPipe implements PipeTransform {
  transform(value: string): string {
    return `My custom transformation of ${value}.`
  }
}
```

### Adding parameters to a custom pipe

You can add parameters to your transformation by adding additional parameters to the `transform` method:

```
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'myCustomTransformation',
})
export class MyCustomTransformationPipe implements PipeTransform {
  transform(value: string, format: string): string {
    let msg = `My custom transformation of ${value}.`

    if (format === 'uppercase') {
      return msg.toUpperCase()
    } else {
      return msg
    }
  }
}
```

### Detecting change within arrays or objects

When you want a pipe to detect changes within arrays or objects, it must be marked as an impure function by passing the `pure` flag with a value of `false`.

Avoid creating impure pipes unless absolutely necessary, as they can incur a significant performance penalty if used without care.

```
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'joinNamesImpure',
  pure: false,
})
export class JoinNamesImpurePipe implements PipeTransform {
  transform(names: string[]): string {
    return names.join();
  }
}
```

Angular developers often adopt the convention of including `Impure` in the pipe `name` and class name to indicate the potential performance pitfall to other developers.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/templates/pipes>
