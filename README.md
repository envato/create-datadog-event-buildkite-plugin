# Create Datadog Event Buildkite Plugin

[Changelog] | [License (MIT)] | [Code of Conduct]

An experimental [Buildkite plugin](https://buildkite.com/docs/agent/v3/plugins) which creates Datadog events.

It contains a [command hook](hooks/command). No tests are currently included, but contributions are welcome.

Inspired by a desire to show releases on metrics graphs, and to include information such as the URL to the build.

## Features

- Creates a Datadog event
- Supports most properties available in the Datadog event API

## Example

```yml
steps:
  - plugins:
      - envato/create-datadog-event#v0.1.0:
          api_key: $DATADOG_API_KEY
          aggregation_key: $BUILDKITE_BUILD_ID
          title: Deploying $BUILDKITE_PIPELINE_SLUG
          text: >
            Deploying $BUILDKITE_BRANCH/$BUILDKITE_COMMIT on behalf of
            $BUILDKITE_BUILD_CREATOR. More details: $BUILDKITE_BUILD_URL
          tags:
            - event-type:deployment
            - state:started
            - branch:$BUILDKITE_BRANCH
    # don't fail the deploy if the event failed
    soft_fail:
      - exit_status: '*'
  
  # deploy step here...
```

Supplying the aggregation key helps if you'd like to emit events for deploy started and deploy succeeded.

## Configuration

Most values correspond to the arguments in the [Post an event API].

| Required | Name      | Description |
| :------: | :-------- | :---------- |
|Y| `api_key`          | Datadog API key for authentication |
|Y| `title`            | Event title, 100 characters max |
|Y| `text`             | Event body as markdown, 4000 characters max |
| | `priority`         | Defaults to `normal`, can change to `low` |
| | `host`             | Host to associate with the event |
| | `tags`             | Array of event tags as strings |
| | `alert_type`       | If an alert event, indicate an `error`, `warning`, `info` or `success` event |
| | `aggregation_key`  | Key used to group related events in the Datadog event stream, 100 characters max |
| | `source_type_name` | Type of event being posted |
| | `related_event_id` | ID of the parent event, integer without quotes |
| | `datadog_host`     | Datadog API URL, e.g. for the European endpoint |

## License

MIT (see [LICENSE](LICENSE))

## Code of Conduct

Contributor Covenant 2.0 (see [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md))

## Maintainers

- [Liam Dawson](https://github.com/liamdawson/)

## About

This project is maintained by the [Envato engineering team][webuild] and funded by [Envato][envato].

[![Envato logo](https://opensource.envato.com/images/envato-oss-readme-logo.png)][envato]

Encouraging the use and creation of open source software is one of the ways we serve our community. See [our other projects][oss] or [come work with us][careers] where you'll find an incredibly diverse, intelligent and capable group of people who help make our company succeed and make our workplace fun, friendly and happy.

  [Post an event API]: https://docs.datadoghq.com/api/?lang=bash#post-an-event
  [Changelog]: CHANGELOG.md
  [License (MIT)]: LICENSE
  [Code of Conduct]: CODE_OF_CONDUCT.md
  [webuild]: http://webuild.envato.com?utm_source=github
  [envato]: https://envato.com?utm_source=github
  [oss]: http://opensource.envato.com//?utm_source=github
  [careers]: http://careers.envato.com/?utm_source=github
