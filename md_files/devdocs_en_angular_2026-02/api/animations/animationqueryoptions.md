# AnimationQueryOptions

AnimationQueryOptions



# AnimationQueryOptions

Encapsulates animation query options. Passed to the [`query()`](query) function.

Deprecation warning

Use `animate.enter` or `animate.leave` instead. Intent to remove in v23

## API

```
interface AnimationQueryOptions extends AnimationOptions {
  optional?: boolean | undefined;
  limit?: number | undefined;
  override delay?: string | number | undefined;
  override params?: { [name: string]: any; } | undefined;
}
```

### optional

`boolean | undefined`

True if this query is optional, false if it is required. Default is false. A required query throws an error if no elements are retrieved when the query is executed. An optional query does not.

### limit

`number | undefined`

A maximum total number of results to return from the query. If negative, results are limited from the end of the query list towards the beginning. By default, results are not limited.

### delay

`string | number | undefined`

Sets a time-delay for initiating an animation action. A number and optional time unit, such as "1s" or "10ms" for one second and 10 milliseconds, respectively.The default unit is milliseconds. Default value is 0, meaning no delay.

### params

`{ [name: string]: any; } | undefined`

A set of developer-defined parameters that modify styling and timing when an animation action starts. An array of key-value pairs, where the provided value is used as a default.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/animations/AnimationQueryOptions>
