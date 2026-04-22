# DATE_PIPE_DEFAULT_OPTIONS

DATE\_PIPE\_DEFAULT\_OPTIONS



# DATE\_PIPE\_DEFAULT\_OPTIONS

DI token that allows to provide default configuration for the [`DatePipe`](datepipe) instances in an application. The value is an object which can include the following fields:

- `dateFormat`: configures the default date format. If not provided, the [`DatePipe`](datepipe) will use the 'mediumDate' as a value.
- `timezone`: configures the default timezone. If not provided, the [`DatePipe`](datepipe) will use the end-user's local system timezone.

[DatePipeConfig](datepipeconfig)

## API

```
const DATE_PIPE_DEFAULT_OPTIONS: InjectionToken<DatePipeConfig>;
```

## Usage Notes

Various date pipe default values can be overwritten by providing this token with the value that has this interface.

For example:

Override the default date format by providing a value using the token:

```
providers: [
  {provide: DATE_PIPE_DEFAULT_OPTIONS, useValue: {dateFormat: 'shortDate'}}
]
```

Override the default timezone by providing a value using the token:

```
providers: [
  {provide: DATE_PIPE_DEFAULT_OPTIONS, useValue: {timezone: '-1200'}}
]
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/common/DATE_PIPE_DEFAULT_OPTIONS>
