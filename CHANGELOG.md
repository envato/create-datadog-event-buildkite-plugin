# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2021-06-07

### Changed

- Escape JSON request body using `python`

  The repositories for Amazon Linux 2 contain jq at version `1.5-1`, whereas the logic in 0.1.0 required functions from `1.6`.

## [0.1.0] - 2021-06-01

### Changed

- Ensure cURL returns an error on a failed request
- Escape JSON request body using `jq`

### Fixed

- Check that a value was provided for the API key

## [0.0.1] - 2020-04-17

### Added

- Initial plugin release
- Limited string escaping for supplied values
- Configuration for most event parameters

[Unreleased]: https://github.com/envato/create-datadog-event-buildkite-plugin/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/envato/create-datadog-event-buildkite-plugin/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/envato/create-datadog-event-buildkite-plugin/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/envato/create-datadog-event-buildkite-plugin/releases/tag/v0.0.1
