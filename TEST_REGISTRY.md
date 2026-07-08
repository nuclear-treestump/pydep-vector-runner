# Test Registry

> Centralized index of all pydepgate tests. Auto-generated; do not edit by hand.
> Run `python scripts/generate_test_registry.py` to regenerate.

**93** test files | **525** test classes | **2428** test cases

---

## Tree

```
└── tests/
    ├── analyzers/
    │   ├── test_analyzer_deepmode.py (17 tests)
    │   ├── test_density_analyzer.py (74 tests)
    │   ├── test_density_enhancement.py (13 tests)
    │   ├── test_dynamic_execution.py (46 tests)
    │   ├── test_encoding_abuse.py (14 tests)
    │   ├── test_resolver.py (68 tests)
    │   ├── test_stdlib_defaults.py (30 tests)
    │   ├── test_string_ops.py (33 tests)
    │   └── test_suspicious_stdlib.py (30 tests)
    ├── api/
    │   └── test_api.py (22 tests)
    ├── cli/
    │   ├── test_cli_workers.py (23 tests)
    │   ├── test_completions.py (33 tests)
    │   ├── test_cvedb_cli.py (15 tests)
    │   ├── test_cvescan.py (9 tests)
    │   ├── test_dispatch.py (8 tests)
    │   ├── test_engine_diagnostics.py (7 tests)
    │   ├── test_env_vars.py (4 tests)
    │   ├── test_extended_sarif.py (21 tests)
    │   ├── test_filtering.py (3 tests)
    │   ├── test_output_formats.py (19 tests)
    │   ├── test_peek_args.py (38 tests)
    │   ├── test_progress.py (25 tests)
    │   ├── test_sarif_args.py (23 tests)
    │   ├── test_scan_loose_file.py (15 tests)
    │   ├── test_scan_single.py (28 tests)
    │   ├── test_subcommand_diag.py (4 tests)
    │   └── test_workers.py (24 tests)
    ├── dbs/
    │   ├── test_pdgdb_extra.py (24 tests)
    │   ├── test_pdgdb_read_write.py (70 tests)
    │   └── test_pdgdb_schema.py (67 tests)
    ├── engines/
    │   ├── test_deploy_the_pickle.py (20 tests)
    │   ├── test_engine_progress.py (8 tests)
    │   ├── test_pipeline.py (17 tests)
    │   └── test_static_engine.py (18 tests)
    ├── enrichers/
    │   ├── test_archive.py (58 tests)
    │   ├── test_asn1.py (110 tests)
    │   ├── test_decode_args.py (31 tests)
    │   ├── test_decode_iocs_mode.py (3 tests)
    │   ├── test_decode_location.py (45 tests)
    │   ├── test_decode_payloads.py (104 tests)
    │   ├── test_enricher_pickle.py (12 tests)
    │   ├── test_enricher_pipeline.py (15 tests)
    │   ├── test_enrichment_hints.py (23 tests)
    │   ├── test_file_hashes.py (8 tests)
    │   ├── test_magic.py (60 tests)
    │   ├── test_new_hashes.py (10 tests)
    │   ├── test_new_iocs.py (18 tests)
    │   ├── test_payload_peek.py (23 tests)
    │   ├── test_pem_detection.py (20 tests)
    │   └── test_unwrap.py (26 tests)
    ├── events/
    │   ├── test_emitter.py (12 tests)
    │   ├── test_envelope.py (12 tests)
    │   ├── test_event_adversarial.py (13 tests)
    │   ├── test_freeze.py (14 tests)
    │   ├── test_scan_granting_ticket.py (13 tests)
    │   └── test_sinks.py (16 tests)
    ├── introspection/
    │   └── test_installed.py (7 tests)
    ├── package_tools/
    │   ├── cvedb/
    │   │   ├── test_fetcher.py (28 tests)
    │   │   ├── test_importer.py (30 tests)
    │   │   ├── test_lookup.py (25 tests)
    │   │   ├── test_pepver.py (30 tests)
    │   │   └── test_schema.py (49 tests)
    │   ├── cvescanner/
    │   │   └── test_scanner.py (10 tests)
    │   ├── depresolution/
    │   │   └── test_deps.py (60 tests)
    │   ├── test_constants.py (19 tests)
    │   └── test_metadata.py (17 tests)
    ├── parsers/
    │   ├── test_pth_parser.py (19 tests)
    │   ├── test_pysource_parser.py (31 tests)
    │   ├── test_sdist.py (4 tests)
    │   └── test_wheel.py (7 tests)
    ├── pdgplatform/
    │   └── test_paths.py (25 tests)
    ├── reporters/
    │   └── sarif/
    │       ├── test_decoded_results.py (83 tests)
    │       ├── test_document.py (50 tests)
    │       ├── test_fingerprints.py (20 tests)
    │       ├── test_render.py (23 tests)
    │       ├── test_results.py (38 tests)
    │       ├── test_rules.py (43 tests)
    │       ├── test_severity.py (24 tests)
    │       └── test_uris.py (19 tests)
    ├── rules/
    │   ├── test_context_predicate.py (44 tests)
    │   ├── test_defaults.py (16 tests)
    │   ├── test_density_deep.py (22 tests)
    │   ├── test_engine_integration.py (3 tests)
    │   ├── test_evaluator.py (16 tests)
    │   ├── test_explain.py (4 tests)
    │   └── test_loader.py (12 tests)
    ├── scanning/
    │   ├── test_static_runner.py (7 tests)
    │   └── test_static_runner_adversarial.py (5 tests)
    ├── traffic_control/
    │   ├── test_traffic_control_deep.py (30 tests)
    │   └── test_traffic_control_triage.py (16 tests)
    ├── visualizers/
    │   ├── test_density_map.py (43 tests)
    │   └── test_peek_render.py (24 tests)
    └── test_run_context.py (9 tests)
```

---

## Contents

- [tests (root)](#tests-root) (9 tests)
- [analyzers](#analyzers) (325 tests)
- [api](#api) (22 tests)
- [cli](#cli) (299 tests)
- [dbs](#dbs) (161 tests)
- [engines](#engines) (63 tests)
- [enrichers](#enrichers) (566 tests)
- [events](#events) (80 tests)
- [introspection](#introspection) (7 tests)
- [package_tools](#package_tools) (36 tests)
- [package_tools/cvedb](#package_toolscvedb) (162 tests)
- [package_tools/cvescanner](#package_toolscvescanner) (10 tests)
- [package_tools/depresolution](#package_toolsdepresolution) (60 tests)
- [parsers](#parsers) (61 tests)
- [pdgplatform](#pdgplatform) (25 tests)
- [reporters/sarif](#reporterssarif) (300 tests)
- [rules](#rules) (117 tests)
- [scanning](#scanning) (12 tests)
- [traffic_control](#traffic_control) (46 tests)
- [visualizers](#visualizers) (67 tests)

---

## tests (root)

*1 files, 9 tests*

### `tests/test_run_context.py` (9 tests)

<details>
<summary><code>TestRunUuidLifecycle</code> (4 tests)</summary>

- `test_first_call_returns_uuid7_string`
- `test_subsequent_calls_return_same_value`
- `test_uuid_is_36_chars_with_hyphens`
- `test_uuid_is_lowercase`

</details>

<details>
<summary><code>TestReset</code> (3 tests)</summary>

- `test_reset_returns_new_uuid`
- `test_reset_changes_subsequent_get`
- `test_reset_without_prior_get_works`

</details>

<details>
<summary><code>TestThreadSafety</code> (1 tests)</summary>

- `test_concurrent_first_access_returns_same_uuid`

</details>

<details>
<summary><code>TestUniqueness</code> (1 tests)</summary>

- `test_resets_produce_different_uuids`

</details>

---

## analyzers

*9 files, 325 tests*

### `tests/analyzers/test_analyzer_deepmode.py` (17 tests)

<details>
<summary><code>DeepModeThreadedToTriageTests</code> (3 tests)</summary>

- `test_deep_engine_classifies_random_py_as_library`
- `test_default_engine_skips_random_py`
- `test_default_engine_default_value_is_false`

</details>

<details>
<summary><code>LibraryPyAnalyzerFilteringTests</code> (3 tests)</summary>

- `test_library_py_runs_only_density_analyzer`
- `test_library_py_does_not_fire_enc001_or_dyn002`
- `test_library_py_still_fires_density_signals`

</details>

<details>
<summary><code>NonLibraryPyKindsUnaffectedTests</code> (2 tests)</summary>

- `test_setup_py_runs_all_analyzers`
- `test_init_py_runs_all_analyzers`

</details>

<details>
<summary><code>DeepVsDefaultEndToEndTests</code> (3 tests)</summary>

- `test_library_file_in_deep_engine_produces_findings`
- `test_library_file_in_default_engine_produces_no_findings`
- `test_setup_py_works_identically_in_both_modes`

</details>

<details>
<summary><code>DeepModePicklabilityTests</code> (2 tests)</summary>

- `test_deep_engine_pickles`
- `test_deep_engine_method_pickles`

</details>

<details>
<summary><code>SelectAnalyzersForKindTests</code> (4 tests)</summary>

- `test_setup_py_returns_all_analyzers`
- `test_library_py_returns_only_density`
- `test_pth_returns_all_analyzers`
- `test_engine_with_no_density_returns_empty_for_library_py`

</details>

### `tests/analyzers/test_density_analyzer.py` (74 tests)

<details>
<summary><code>ShannonEntropyTests</code> (4 tests)</summary>

- `test_empty_string_is_zero`
- `test_single_repeated_char_is_zero`
- `test_uniform_distribution_matches_log2`
- `test_high_entropy_string_above_threshold`

</details>

<details>
<summary><code>VowelRatioTests</code> (4 tests)</summary>

- `test_all_vowels`
- `test_no_vowels`
- `test_mixed`
- `test_empty`

</details>

<details>
<summary><code>MaxAstDepthTests</code> (2 tests)</summary>

- `test_flat_module_depth_low`
- `test_deeply_nested_lists_increase_depth`

</details>

<details>
<summary><code>CleanCodeTests</code> (3 tests)</summary>

- `test_simple_code_no_signals`
- `test_short_strings_below_entropy_minimum`
- `test_normal_identifiers_no_dens020`

</details>

<details>
<summary><code>TokenDensityTests</code> (3 tests)</summary>

- `test_dense_line_fires_dens001_medium`
- `test_very_dense_line_fires_dens001_high`
- `test_short_lines_do_not_fire`

</details>

<details>
<summary><code>SemicolonTests</code> (4 tests)</summary>

- `test_single_semicolon_fires_medium`
- `test_three_semicolons_fires_high`
- `test_no_semicolon_does_not_fire`
- `test_semicolon_inside_string_does_not_fire`

</details>

<details>
<summary><code>StringEntropyTests</code> (5 tests)</summary>

- `test_high_entropy_string_fires_dens010`
- `test_long_high_entropy_string_fires_high`
- `test_low_entropy_long_string_does_not_fire`
- `test_short_high_entropy_string_does_not_fire`
- `test_dens010_includes_entropy_in_context`

</details>

<details>
<summary><code>Base64AlphabetTests</code> (3 tests)</summary>

- `test_b64_alphabet_string_fires_dens011`
- `test_b64_string_missing_digits_does_not_fire`
- `test_b64_string_with_non_alphabet_char_does_not_fire`

</details>

<details>
<summary><code>VowelRatioIdentifierTests</code> (5 tests)</summary>

- `test_long_vowelless_identifier_fires`
- `test_short_low_vowel_identifier_does_not_fire`
- `test_dunder_skipped`
- `test_skip_listed_identifier_not_flagged`
- `test_normal_identifiers_do_not_fire`

</details>

<details>
<summary><code>ConfusableSingleCharTests</code> (5 tests)</summary>

- `test_lowercase_l_fires`
- `test_capital_o_fires`
- `test_capital_i_fires`
- `test_two_char_name_does_not_fire`
- `test_normal_short_name_does_not_fire`

</details>

<details>
<summary><code>InvisibleUnicodeTests</code> (4 tests)</summary>

- `test_zero_width_space_fires`
- `test_rtl_override_fires_definite`
- `test_multiple_invisibles_on_same_line_only_fire_once`
- `test_multiple_invisibles_across_lines_fire_separately`

</details>

<details>
<summary><code>HomoglyphTests</code> (3 tests)</summary>

- `test_cyrillic_a_fires`
- `test_greek_omicron_fires`
- `test_pure_ascii_does_not_fire`

</details>

<details>
<summary><code>AstDepthTests</code> (3 tests)</summary>

- `test_deeply_nested_one_liner_fires`
- `test_normal_balanced_code_does_not_fire`
- `test_tiny_file_does_not_fire`

</details>

<details>
<summary><code>NestedLambdaTests</code> (3 tests)</summary>

- `test_four_deep_lambda_fires`
- `test_two_deep_lambda_does_not_fire`
- `test_nested_comprehensions_fire`

</details>

<details>
<summary><code>IntegerArrayTests</code> (5 tests)</summary>

- `test_byte_range_list_fires`
- `test_byte_range_tuple_fires`
- `test_short_list_does_not_fire`
- `test_out_of_range_list_does_not_fire`
- `test_mixed_types_below_ratio_threshold_does_not_fire`

</details>

<details>
<summary><code>DocstringEntropyTests</code> (4 tests)</summary>

- `test_high_entropy_module_docstring_fires`
- `test_normal_docstring_does_not_fire`
- `test_high_entropy_function_docstring_fires`
- `test_high_entropy_docstring_does_not_also_fire_dens010`

</details>

<details>
<summary><code>DynamicDocTests</code> (4 tests)</summary>

- `test_exec_doc_fires`
- `test_attribute_doc_fires`
- `test_unrelated_dunder_does_not_fire`
- `test_doc_without_call_does_not_fire`

</details>

<details>
<summary><code>RobustnessTests</code> (3 tests)</summary>

- `test_unparseable_source_still_runs_token_layer`
- `test_empty_source_produces_no_signals`
- `test_random_bytes_does_not_crash`

</details>

<details>
<summary><code>PthExecLineTests</code> (5 tests)</summary>

- `test_pth_dense_line_fires_dens001`
- `test_pth_semicolon_chain_fires_dens002`
- `test_pth_b64_string_fires`
- `test_pth_invisible_unicode_fires`
- `test_pth_does_not_emit_dens020_or_dens050`

</details>

<details>
<summary><code>ScopeReportingTests</code> (2 tests)</summary>

- `test_module_scope_reported_for_module_level_string`
- `test_function_scope_reported`

</details>

### `tests/analyzers/test_density_enhancement.py` (13 tests)

<details>
<summary><code>BareDocAtModuleLevelTests</code> (4 tests)</summary>

- `test_prose_module_docstring_suppresses`
- `test_encoded_module_docstring_emits`
- `test_python_source_module_docstring_emits`
- `test_no_module_docstring_emits`

</details>

<details>
<summary><code>BareDocInsideFunctionTests</code> (2 tests)</summary>

- `test_function_body_uses_module_doc`
- `test_function_body_with_encoded_module_doc`

</details>

<details>
<summary><code>BareDocInsideClassTests</code> (2 tests)</summary>

- `test_class_body_uses_class_doc`
- `test_method_body_falls_through_to_module`

</details>

<details>
<summary><code>AttributeDocReferenceTests</code> (4 tests)</summary>

- `test_resolved_function_with_prose_doc_suppresses`
- `test_resolved_class_with_prose_doc_suppresses`
- `test_resolved_function_with_encoded_doc_emits`
- `test_unresolvable_attribute_emits`

</details>

<details>
<summary><code>ScipyStyleDocformatTests</code> (1 tests)</summary>

- `test_scipy_pattern_suppresses`

</details>

### `tests/analyzers/test_dynamic_execution.py` (46 tests)

<details>
<summary><code>HappyPathDirectExecTests</code> (7 tests)</summary>

- `test_module_level_exec_with_literal_fires_dyn001`
- `test_module_level_exec_with_variable_fires_dyn002`
- `test_module_level_eval_with_call_argument_fires_dyn002`
- `test_module_level_eval_with_fstring_fires_dyn002`
- `test_module_level_exec_with_binop_fires_dyn002`
- `test_function_level_exec_with_variable_fires_dyn003`
- `test_function_level_exec_with_literal_does_not_fire`

</details>

<details>
<summary><code>HappyPathDynamicImportTests</code> (3 tests)</summary>

- `test_underscore_import_with_variable_fires_dyn004`
- `test_importlib_with_variable_fires_dyn004`
- `test_underscore_import_with_literal_does_not_fire`

</details>

<details>
<summary><code>HappyPathBuiltinsAccessTests</code> (5 tests)</summary>

- `test_getattr_builtins_eval_fires_dyn005`
- `test_getattr_builtins_module_form_fires_dyn005`
- `test_globals_subscript_eval_fires_dyn005`
- `test_locals_subscript_exec_fires_dyn005`
- `test_vars_subscript_compile_fires_dyn005`

</details>

<details>
<summary><code>HappyPathCompileThenExecTests</code> (4 tests)</summary>

- `test_compile_then_exec_fires_dyn006`
- `test_compile_with_exec_mode_fires_precursor`
- `test_compile_with_eval_mode_does_not_fire_precursor`
- `test_compile_then_eval_fires_dyn006`

</details>

<details>
<summary><code>HappyPathAliasedShapeTests</code> (2 tests)</summary>

- `test_aliased_call_with_decode_argument_fires_dyn007`
- `test_aliased_zlib_decompress_fires_dyn007`

</details>

<details>
<summary><code>EvasionAliasingTests</code> (3 tests)</summary>

- `test_simple_alias_caught_by_dyn007`
- `test_module_alias_call`
- `test_attribute_alias_call`

</details>

<details>
<summary><code>EvasionBuiltinsTests</code> (2 tests)</summary>

- `test_builtins_dict_form`
- `test_double_indirection`

</details>

<details>
<summary><code>EvasionStringObfuscationTests</code> (2 tests)</summary>

- `test_chr_concatenation_does_not_crash`
- `test_string_split_does_not_crash`

</details>

<details>
<summary><code>EvasionTwoStepReassignTests</code> (2 tests)</summary>

- `test_compile_then_reassign_then_exec_still_flags`
- `test_compile_in_one_function_exec_in_another`

</details>

<details>
<summary><code>EvasionSyntaxLayoutTests</code> (3 tests)</summary>

- `test_exec_call_on_one_line_with_semicolons`
- `test_exec_inside_walrus`
- `test_exec_inside_lambda`

</details>

<details>
<summary><code>FalsePositiveBattery</code> (7 tests)</summary>

- `test_legitimate_compile_with_eval_mode_no_following_exec`
- `test_function_with_legitimate_eval_use`
- `test_print_with_decoded_data_does_not_fire_dyn007`
- `test_len_of_decoded_does_not_fire_dyn007`
- `test_static_string_compile_no_exec_fires_only_precursor`
- `test_clean_module_produces_no_signals`
- `test_normal_function_definitions_produce_no_signals`

</details>

<details>
<summary><code>RobustnessTests</code> (6 tests)</summary>

- `test_unparseable_source_produces_no_signals`
- `test_empty_source_produces_no_signals`
- `test_exec_with_no_arguments_does_not_crash`
- `test_getattr_with_no_arguments_does_not_crash`
- `test_subscript_with_non_literal_does_not_crash`
- `test_deeply_nested_calls_do_not_crash`

</details>

### `tests/analyzers/test_encoding_abuse.py` (14 tests)

<details>
<summary><code>EncodingAbuseDetectionTests</code> (11 tests)</summary>

- `test_clean_code_produces_no_signals`
- `test_plain_base64_decode_produces_no_signal`
- `test_exec_base64_literal_fires_definite`
- `test_exec_long_base64_literal_fires_definite`
- `test_eval_zlib_decompress_fires`
- `test_compile_with_hex_decode_fires`
- `test_decode_inside_function_uses_function_scope`
- `test_decode_inside_nested_function`
- `test_decode_inside_class_body`
- `test_location_is_reported`
- `test_unparseable_source_produces_no_signals`

</details>

<details>
<summary><code>EncodingAbuseNonTriggersTests</code> (3 tests)</summary>

- `test_string_concatenation_is_not_a_payload_literal`
- `test_ordinary_hex_is_not_a_signal`
- `test_exec_without_decode_is_different_concern`

</details>

### `tests/analyzers/test_resolver.py` (68 tests)

<details>
<summary><code>SafetyTests</code> (6 tests)</summary>

- `test_does_not_execute_function_calls`
- `test_does_not_evaluate_arbitrary_calls`
- `test_handles_malformed_chr_argument`
- `test_handles_chr_out_of_range`
- `test_handles_huge_string_multiplication`
- `test_handles_huge_int_arithmetic`

</details>

<details>
<summary><code>ConstantTests</code> (6 tests)</summary>

- `test_string_literal`
- `test_bytes_literal`
- `test_integer_literal`
- `test_negative_integer_literal`
- `test_none_literal`
- `test_bool_literal`

</details>

<details>
<summary><code>StringConcatTests</code> (4 tests)</summary>

- `test_simple_concat`
- `test_three_piece_concat`
- `test_concat_with_chr`
- `test_string_multiplication`

</details>

<details>
<summary><code>BytesTests</code> (6 tests)</summary>

- `test_bytes_concat`
- `test_bytes_from_list`
- `test_bytes_fromhex`
- `test_bytes_decode`
- `test_bytes_decode_with_encoding`
- `test_bytes_decode_unsupported_encoding`

</details>

<details>
<summary><code>ChrOrdTests</code> (3 tests)</summary>

- `test_chr`
- `test_chr_with_arithmetic`
- `test_ord`

</details>

<details>
<summary><code>SliceTests</code> (3 tests)</summary>

- `test_slice_reverse`
- `test_slice_range`
- `test_index_access`

</details>

<details>
<summary><code>JoinReplaceTests</code> (3 tests)</summary>

- `test_empty_join`
- `test_separator_join`
- `test_replace`

</details>

<details>
<summary><code>VariableTrackingTests</code> (4 tests)</summary>

- `test_resolved_variable`
- `test_unresolved_variable`
- `test_ambiguous_variable`
- `test_variable_in_concat`

</details>

<details>
<summary><code>PartialResolutionTests</code> (4 tests)</summary>

- `test_unresolved_variable_in_concat_produces_partial`
- `test_unresolved_function_call_produces_partial`
- `test_fstring_with_unresolved_interpolation`
- `test_unresolved_fragments_recorded`

</details>

<details>
<summary><code>FStringTests</code> (5 tests)</summary>

- `test_fstring_with_no_interpolation`
- `test_fstring_with_literal_interpolation`
- `test_fstring_with_resolved_variable`
- `test_fstring_with_format_spec_unresolved`
- `test_fstring_with_conversion_unresolved`

</details>

<details>
<summary><code>AdversarialTests</code> (4 tests)</summary>

- `test_deeply_nested_concat`
- `test_extremely_deep_recursion_aborts`
- `test_unmodeled_expression_returns_partial`
- `test_dict_literal_unmodeled`

</details>

<details>
<summary><code>OperationsTrackingTests</code> (4 tests)</summary>

- `test_simple_constant_has_one_operation`
- `test_concat_records_operations`
- `test_chr_concat_has_many_operations`
- `test_bytes_decode_operation_recorded`

</details>

<details>
<summary><code>RealWorldPatternTests</code> (6 tests)</summary>

- `test_eval_assembled_from_chars`
- `test_exec_via_reverse`
- `test_compile_assembled_via_concat`
- `test_import_via_join`
- `test_os_via_bytes_fromhex`
- `test_eval_via_bytes_then_decode`

</details>

<details>
<summary><code>FragmentTrackingTests</code> (10 tests)</summary>

- `test_constant_has_single_fragment`
- `test_concat_has_single_fragment_of_concatenated_value`
- `test_partial_concat_carries_resolved_pieces`
- `test_partial_chr_concat_carries_chr_results`
- `test_partial_concat_preserves_order`
- `test_partial_fstring_carries_resolved_pieces`
- `test_int_resolution_has_str_coerced_fragment`
- `test_unresolved_root_has_empty_fragments`
- `test_concatenation_with_chr_in_one_position`
- `test_three_way_partial_with_two_resolved`

</details>

### `tests/analyzers/test_stdlib_defaults.py` (30 tests)

<details>
<summary><code>ProcessSpawnTests</code> (9 tests)</summary>

- `test_subprocess_popen_fires`
- `test_subprocess_run_fires`
- `test_subprocess_check_output_fires`
- `test_os_system_fires`
- `test_os_popen_fires`
- `test_os_execv_fires`
- `test_os_fork_fires`
- `test_module_scope_recorded`
- `test_function_scope_recorded`

</details>

<details>
<summary><code>NetworkAccessTests</code> (6 tests)</summary>

- `test_urllib_urlopen_fires`
- `test_urllib_urlretrieve_fires`
- `test_socket_socket_fires`
- `test_http_client_fires`
- `test_ftplib_fires`
- `test_smtplib_fires`

</details>

<details>
<summary><code>NativeLoadTests</code> (3 tests)</summary>

- `test_ctypes_cdll_fires`
- `test_ctypes_windll_fires`
- `test_ctypes_cdll_loadlibrary_fires`

</details>

<details>
<summary><code>FalsePositiveBattery</code> (5 tests)</summary>

- `test_import_alone_does_not_fire`
- `test_subprocess_attribute_access_does_not_fire`
- `test_string_mentioning_subprocess_does_not_fire`
- `test_unrelated_code_produces_no_signals`
- `test_aliased_import_misses_known_limitation`

</details>

<details>
<summary><code>RobustnessTests</code> (4 tests)</summary>

- `test_unparseable_source_produces_no_signals`
- `test_empty_source_produces_no_signals`
- `test_call_with_zero_args_does_not_crash`
- `test_nested_calls_produce_correct_signals`

</details>

<details>
<summary><code>RealWorldPatternTests</code> (3 tests)</summary>

- `test_setup_py_curl_pattern`
- `test_setup_py_data_exfil_pattern`
- `test_init_py_native_load`

</details>

### `tests/analyzers/test_string_ops.py` (33 tests)

<details>
<summary><code>StandaloneObfuscationTests</code> (2 tests)</summary>

- `test_concat_resolves_to_eval`
- `test_standalone_expression_statement_with_obfuscation`

</details>

<details>
<summary><code>DangerousCallObfuscationTests</code> (7 tests)</summary>

- `test_getattr_with_concat_eval_fires`
- `test_getattr_with_chr_concat_eval_fires_definite`
- `test_getattr_with_reverse_eval_fires`
- `test_globals_subscript_with_concat_eval_fires`
- `test_builtins_dict_subscript_with_concat_fires`
- `test_import_module_with_obfuscated_module_name`
- `test_underscore_import_with_chr_assembled_name`

</details>

<details>
<summary><code>CrossReferenceTests</code> (3 tests)</summary>

- `test_assigned_name_used_in_getattr_fires_str003`
- `test_chr_assembled_name_used_in_import_fires_str003`
- `test_reassigned_variable_does_not_fire_str003`

</details>

<details>
<summary><code>HeavyObfuscationTests</code> (1 tests)</summary>

- `test_heavy_chr_chain_with_unresolved_var_fires_str004`

</details>

<details>
<summary><code>PartialResolutionTests</code> (2 tests)</summary>

- `test_partial_resolution_with_sensitive_fragment`
- `test_partial_resolution_no_sensitive_fragment`

</details>

<details>
<summary><code>FalsePositiveBattery</code> (8 tests)</summary>

- `test_legitimate_concat_to_non_sensitive_name`
- `test_chr_used_for_crlf`
- `test_join_used_for_csv`
- `test_string_reverse_for_palindrome`
- `test_legitimate_getattr_with_literal`
- `test_legitimate_getattr_on_user_object`
- `test_clean_module_produces_no_signals`
- `test_format_string_with_literal_sensitive_substring`

</details>

<details>
<summary><code>RobustnessTests</code> (6 tests)</summary>

- `test_unparseable_source_produces_no_signals`
- `test_empty_source_produces_no_signals`
- `test_getattr_with_no_args_does_not_crash`
- `test_getattr_with_one_arg_does_not_crash`
- `test_unknown_call_does_not_crash`
- `test_deeply_nested_concat_does_not_crash`

</details>

<details>
<summary><code>RealWorldPatternTests</code> (4 tests)</summary>

- `test_classic_eval_via_chr_concat_in_getattr`
- `test_os_via_subscript_with_reverse`
- `test_subprocess_via_join`
- `test_compile_via_bytes_decode`

</details>

### `tests/analyzers/test_suspicious_stdlib.py` (30 tests)

<details>
<summary><code>ProcessSpawnTests</code> (9 tests)</summary>

- `test_subprocess_popen_fires`
- `test_subprocess_run_fires`
- `test_subprocess_check_output_fires`
- `test_os_system_fires`
- `test_os_popen_fires`
- `test_os_execv_fires`
- `test_os_fork_fires`
- `test_module_scope_recorded`
- `test_function_scope_recorded`

</details>

<details>
<summary><code>NetworkAccessTests</code> (6 tests)</summary>

- `test_urllib_urlopen_fires`
- `test_urllib_urlretrieve_fires`
- `test_socket_socket_fires`
- `test_http_client_fires`
- `test_ftplib_fires`
- `test_smtplib_fires`

</details>

<details>
<summary><code>NativeLoadTests</code> (3 tests)</summary>

- `test_ctypes_cdll_fires`
- `test_ctypes_windll_fires`
- `test_ctypes_cdll_loadlibrary_fires`

</details>

<details>
<summary><code>FalsePositiveBattery</code> (5 tests)</summary>

- `test_import_alone_does_not_fire`
- `test_subprocess_attribute_access_does_not_fire`
- `test_string_mentioning_subprocess_does_not_fire`
- `test_unrelated_code_produces_no_signals`
- `test_aliased_import_misses_known_limitation`

</details>

<details>
<summary><code>RobustnessTests</code> (4 tests)</summary>

- `test_unparseable_source_produces_no_signals`
- `test_empty_source_produces_no_signals`
- `test_call_with_zero_args_does_not_crash`
- `test_nested_calls_produce_correct_signals`

</details>

<details>
<summary><code>RealWorldPatternTests</code> (3 tests)</summary>

- `test_setup_py_curl_pattern`
- `test_setup_py_data_exfil_pattern`
- `test_init_py_native_load`

</details>

---

## api

*1 files, 22 tests*

### `tests/api/test_api.py` (22 tests)

<details>
<summary><code>ApiValidationTests</code> (8 tests)</summary>

- `test_single_true_is_blocked_for_archive_targets`
- `test_invalid_mode_is_rejected`
- `test_url_targets_are_rejected_until_intake_exists`
- `test_decode_iocs_requires_known_mode`
- `test_decode_iocs_requires_decode_enabled`
- `test_single_and_deep_are_rejected_together`
- `test_as_kind_requires_single_mode`
- `test_output_format_validation_and_human_alias`

</details>

<details>
<summary><code>ApiSafeFindingTests</code> (2 tests)</summary>

- `test_sanitize_mapping_preserves_bounded_decoded_preview`
- `test_sanitize_mapping_removes_nested_private_keys`

</details>

<details>
<summary><code>ApiScanResultTests</code> (11 tests)</summary>

- `test_repr_is_compact_and_does_not_dump_native_objects`
- `test_summary_contains_expected_public_fields`
- `test_public_internals_are_blocked`
- `test_unsafe_getters_require_exact_tokens`
- `test_hashes_mode_decoded_tree_does_not_retain_decoded_source`
- `test_safe_findings_do_not_contain_full_payload_material`
- `test_iocs_are_hash_only_public_records`
- `test_event_log_contains_ordered_lifecycle_and_decode_summary`
- `test_renderers_parse_and_do_not_leak_full_payload_material`
- `test_write_report_and_iocs_create_files`
- `test_payload_archive_export_is_blocked_in_hashes_mode`

</details>

<details>
<summary><code>ApiFullModeTests</code> (1 tests)</summary>

- `test_full_mode_required_for_payload_archive_export`

</details>

---

## cli

*17 files, 299 tests*

### `tests/cli/test_cli_workers.py` (23 tests)

<details>
<summary><code>WorkersDefaultFromEnvTests</code> (11 tests)</summary>

- `test_env_unset_returns_none`
- `test_env_empty_string_returns_none`
- `test_env_whitespace_only_returns_none`
- `test_env_serial`
- `test_env_auto`
- `test_env_integer`
- `test_env_integer_with_surrounding_whitespace`
- `test_env_invalid_string_silently_ignored`
- `test_env_zero_silently_ignored`
- `test_env_negative_silently_ignored`
- `test_env_float_silently_ignored`

</details>

<details>
<summary><code>WorkersEnvParserIntegrationTests</code> (7 tests)</summary>

- `test_env_serial_becomes_args_workers`
- `test_env_integer_becomes_args_workers`
- `test_env_auto_becomes_args_workers`
- `test_env_unset_args_workers_is_none`
- `test_env_bogus_args_workers_is_none`
- `test_cli_flag_overrides_env_at_top_level`
- `test_cli_flag_overrides_env_at_subcommand_position`

</details>

<details>
<summary><code>ForceParallelEnvDefaultTests</code> (5 tests)</summary>

- `test_env_unset_false`
- `test_env_truthy_values_all_read_true`
- `test_env_falsy_values_all_read_false`
- `test_cli_flag_overrides_env_at_top_level`
- `test_cli_flag_overrides_env_at_subcommand_position`

</details>

### `tests/cli/test_completions.py` (33 tests)

<details>
<summary><code>SubcommandCompletionTests</code> (5 tests)</summary>

- `test_empty_offers_visible_subcommands`
- `test_hidden_complete_subcommand_not_offered`
- `test_partial_match_filters`
- `test_no_partial_match_returns_empty`
- `test_subcommand_after_global_flag_still_completes`

</details>

<details>
<summary><code>FlagNameCompletionTests</code> (5 tests)</summary>

- `test_global_flags_at_top_level`
- `test_global_flags_after_subcommand`
- `test_scan_specific_flags_only_in_scan_context`
- `test_partial_flag_match`
- `test_top_level_only_flag_not_offered_inside_subcommand`

</details>

<details>
<summary><code>FlagValueCompletionTests</code> (7 tests)</summary>

- `test_format_values`
- `test_color_values`
- `test_min_severity_values`
- `test_as_kind_values`
- `test_format_value_partial_match`
- `test_free_form_value_returns_empty`
- `test_integer_value_returns_empty`

</details>

<details>
<summary><code>PositionalCompletionTests</code> (4 tests)</summary>

- `test_help_topic_offers_subcommand_names`
- `test_help_topic_partial_match`
- `test_completions_offers_supported_shells`
- `test_completions_partial_match`

</details>

<details>
<summary><code>FreeFormPositionalTests</code> (2 tests)</summary>

- `test_scan_target_returns_empty`
- `test_exec_script_returns_empty`

</details>

<details>
<summary><code>FlagValueOverridesEverythingElseTests</code> (2 tests)</summary>

- `test_flag_value_completion_wins_over_subcommand_logic`
- `test_flag_value_completion_works_at_top_level_too`

</details>

<details>
<summary><code>SubcommandDetectionTests</code> (2 tests)</summary>

- `test_subcommand_skipped_after_path_value_flag`
- `test_subcommand_skipped_after_choice_value_flag`

</details>

<details>
<summary><code>ScriptGenerationTests</code> (6 tests)</summary>

- `test_bash_script_contains_expected_pieces`
- `test_zsh_script_contains_expected_pieces`
- `test_fish_script_contains_expected_pieces`
- `test_script_for_shell_dispatches_correctly`
- `test_script_for_shell_unknown_raises`
- `test_supported_shells_matches_dispatcher`

</details>

### `tests/cli/test_cvedb_cli.py` (15 tests)

<details>
<summary><code>TestRegister</code> (5 tests)</summary>

- `test_register_creates_cvedb_subcommand`
- `test_cvedb_accepts_valid_actions`
- `test_cvedb_rejects_unknown_action`
- `test_cvedb_no_bar_flag`
- `test_cvedb_no_bar_defaults_false`

</details>

<details>
<summary><code>TestPathAction</code> (1 tests)</summary>

- `test_path_prints_db_location`

</details>

<details>
<summary><code>TestStatusAction</code> (2 tests)</summary>

- `test_status_when_db_does_not_exist`
- `test_status_with_populated_db`

</details>

<details>
<summary><code>TestUpdateAction</code> (6 tests)</summary>

- `test_update_happy_path`
- `test_update_summary_total_is_sum`
- `test_update_head_check_failure`
- `test_update_size_limit_exceeded`
- `test_update_download_failure`
- `test_update_existing_db_preserved_on_failure`

</details>

<details>
<summary><code>TestDispatchDefensive</code> (1 tests)</summary>

- `test_run_with_unknown_action_returns_tool_error`

</details>

### `tests/cli/test_cvescan.py` (9 tests)

<details>
<summary><code>CveScanCliTests</code> (9 tests)</summary>

- `test_register_creates_cvescan_subcommand`
- `test_main_parser_dispatches_cvescan`
- `test_human_output_returns_blocking_for_high_finding`
- `test_json_output_contains_finding_and_metadata`
- `test_min_severity_filters_display_and_exit_code`
- `test_strict_exit_uses_hidden_findings`
- `test_missing_database_is_tool_error_by_default`
- `test_ignore_missing_database_returns_warning_result`
- `test_sarif_output_is_rejected`

</details>

### `tests/cli/test_dispatch.py` (8 tests)

<details>
<summary><code>NoArgumentsTests</code> (2 tests)</summary>

- `test_no_args_prints_help`
- `test_help_flag`

</details>

<details>
<summary><code>VersionTests</code> (2 tests)</summary>

- `test_version_subcommand`
- `test_version_flag`

</details>

<details>
<summary><code>StubsTests</code> (2 tests)</summary>

- `test_exec_stub_explains_under_development`
- `test_preflight_stub_explains_under_development`

</details>

<details>
<summary><code>ScanDispatchTests</code> (2 tests)</summary>

- `test_scan_installed_package_pip`
- `test_scan_nonexistent_package_returns_tool_error`

</details>

### `tests/cli/test_engine_diagnostics.py` (7 tests)

<details>
<summary><code>ScanFileErrorPathTests</code> (1 tests)</summary>

- `test_missing_file_includes_initial_diagnostics`

</details>

<details>
<summary><code>ScanLooseFileAsErrorPathTests</code> (1 tests)</summary>

- `test_missing_file_includes_initial_diagnostics`

</details>

<details>
<summary><code>ScanInstalledErrorPathTests</code> (1 tests)</summary>

- `test_missing_package_includes_initial_diagnostics`

</details>

<details>
<summary><code>EnumerateFailurePathTests</code> (1 tests)</summary>

- `test_enumerate_exception_includes_initial_diagnostics`

</details>

<details>
<summary><code>AggregateSuccessPathTests</code> (1 tests)</summary>

- `test_success_path_includes_initial_diagnostics`

</details>

<details>
<summary><code>WrapSingleOutputPathTests</code> (1 tests)</summary>

- `test_scan_bytes_includes_initial_diagnostics`

</details>

<details>
<summary><code>DefaultBehaviorPreservationTests</code> (1 tests)</summary>

- `test_default_empty_no_extra_diagnostics`

</details>

### `tests/cli/test_env_vars.py` (4 tests)

<details>
<summary><code>EnvVarTests</code> (4 tests)</summary>

- `test_pydepgate_format_env_var`
- `test_pydepgate_ci_env_var`
- `test_no_color_env_var_respected`
- `test_explicit_flag_overrides_env_var`

</details>

### `tests/cli/test_extended_sarif.py` (21 tests)

<details>
<summary><code>SarifScanModeTests</code> (5 tests)</summary>

- `test_returns_none_when_deep_false`
- `test_returns_wheel_deep_for_deep_wheel`
- `test_returns_sdist_deep_for_deep_sdist`
- `test_returns_installed_env_deep_for_deep_installed`
- `test_handles_missing_deep_attr_gracefully`

</details>

<details>
<summary><code>ComputeDecodedTreeTests</code> (8 tests)</summary>

- `test_returns_tree_on_success`
- `test_returns_none_on_decode_exception`
- `test_writes_warning_on_decode_exception`
- `test_warning_includes_exception_type_and_message`
- `test_applies_min_severity_filter_when_set`
- `test_does_not_apply_filter_when_min_severity_unset`
- `test_decode_payloads_receives_correct_kwargs`
- `test_extract_iocs_false_when_mode_is_off`

</details>

<details>
<summary><code>SarifIntegrationTests</code> (8 tests)</summary>

- `test_sarif_with_srcroot_propagates_to_uri_base_ids`
- `test_sarif_srcroot_via_env_var`
- `test_sarif_srcroot_cli_overrides_env_var`
- `test_srcroot_warning_when_format_is_json`
- `test_srcroot_no_warning_when_format_is_sarif`
- `test_sarif_clean_scan_uri_is_empty_placeholder`
- `test_sarif_clean_scan_automation_details`
- `test_sarif_with_decode_payload_runs_cleanly`

</details>

### `tests/cli/test_filtering.py` (3 tests)

<details>
<summary><code>CiModeTests</code> (1 tests)</summary>

- `test_ci_mode_uses_json_format_by_default`

</details>

<details>
<summary><code>MinSeverityTests</code> (1 tests)</summary>

- `test_min_severity_high_filters_low_findings`

</details>

<details>
<summary><code>StrictExitTests</code> (1 tests)</summary>

- `test_strict_exit_flag_accepted`

</details>

### `tests/cli/test_output_formats.py` (19 tests)

<details>
<summary><code>JsonFormatTests</code> (2 tests)</summary>

- `test_scan_pip_json_output_is_valid_json`
- `test_json_schema_has_expected_top_level_keys`

</details>

<details>
<summary><code>HumanFormatTests</code> (1 tests)</summary>

- `test_human_format_clean_scan`

</details>

<details>
<summary><code>SarifFormatTests</code> (1 tests)</summary>

- `test_sarif_format_clean_scan`

</details>

<details>
<summary><code>ColorFlagTests</code> (15 tests)</summary>

- `test_color_auto_accepted`
- `test_color_always_accepted`
- `test_color_never_accepted`
- `test_invalid_color_value_rejected`
- `test_no_color_alias_still_works`
- `test_no_color_produces_same_output_as_color_never`
- `test_color_always_emits_ansi_under_redirection`
- `test_color_never_suppresses_ansi`
- `test_color_auto_suppresses_ansi_under_redirection`
- `test_pydepgate_color_env_var_used_as_default`
- `test_explicit_cli_color_overrides_env`
- `test_no_color_env_implies_never`
- `test_color_always_overrides_no_color_env`
- `test_pydepgate_no_color_env_implies_never`
- `test_ci_mode_disables_color_by_default`

</details>

### `tests/cli/test_peek_args.py` (38 tests)

<details>
<summary><code>DefaultArgumentParsingTests</code> (6 tests)</summary>

- `test_no_args_yields_disabled_peek`
- `test_peek_flag_enables`
- `test_peek_chain_flag`
- `test_explicit_depth_override`
- `test_explicit_budget_override`
- `test_explicit_min_length_override`

</details>

<details>
<summary><code>EnvironmentVariableDefaultsTests</code> (8 tests)</summary>

- `test_env_peek_truthy_enables_default`
- `test_env_peek_falsy_keeps_disabled`
- `test_env_peek_depth_used_as_default`
- `test_env_peek_budget_used_as_default`
- `test_env_peek_min_length_used_as_default`
- `test_env_peek_chain_truthy`
- `test_malformed_int_env_uses_default_with_warning`
- `test_malformed_min_length_env_uses_default_with_warning`

</details>

<details>
<summary><code>CliOverridesEnvTests</code> (3 tests)</summary>

- `test_cli_depth_overrides_env`
- `test_cli_peek_overrides_env_disabled`
- `test_cli_min_length_overrides_env`

</details>

<details>
<summary><code>SoftWarningTests</code> (7 tests)</summary>

- `test_no_warning_when_only_defaults`
- `test_warning_when_depth_set_without_peek`
- `test_warning_when_budget_set_without_peek`
- `test_warning_when_min_length_set_without_peek`
- `test_warning_when_chain_set_without_peek`
- `test_warning_lists_multiple_ignored_flags`
- `test_no_warning_when_peek_enabled_and_tuning_set`

</details>

<details>
<summary><code>HardErrorTests</code> (7 tests)</summary>

- `test_depth_zero_raises_when_peek_enabled`
- `test_depth_above_ceiling_raises`
- `test_budget_below_floor_raises`
- `test_min_length_below_floor_raises`
- `test_min_length_at_floor_allowed`
- `test_out_of_range_does_not_raise_when_peek_disabled`
- `test_min_length_below_floor_does_not_raise_when_peek_disabled`

</details>

<details>
<summary><code>BuildPeekEnricherTests</code> (4 tests)</summary>

- `test_returns_none_when_peek_disabled`
- `test_returns_configured_enricher_when_enabled`
- `test_returns_default_enricher_when_no_tuning`
- `test_min_length_threaded_through_to_enricher`

</details>

<details>
<summary><code>PeekChainEnabledTests</code> (3 tests)</summary>

- `test_false_when_peek_off`
- `test_false_when_chain_off`
- `test_true_when_both_on`

</details>

### `tests/cli/test_progress.py` (25 tests)

<details>
<summary><code>TestProgressBarRendering</code> (5 tests)</summary>

- `test_renders_on_first_update`
- `test_uses_custom_label`
- `test_final_state_is_all_equals`
- `test_intermediate_state_has_progress_marker`
- `test_pads_to_clear_previous_longer_line`

</details>

<details>
<summary><code>TestProgressBarThrottling</code> (4 tests)</summary>

- `test_throttle_suppresses_rapid_intermediate_updates`
- `test_throttle_does_not_suppress_first_update`
- `test_throttle_does_not_suppress_final_update`
- `test_throttle_lets_through_after_interval`

</details>

<details>
<summary><code>TestProgressBarDisabled</code> (3 tests)</summary>

- `test_force_disabled_writes_nothing`
- `test_non_tty_stream_auto_disables`
- `test_tty_stream_auto_enables`

</details>

<details>
<summary><code>TestProgressBarEdgeCases</code> (7 tests)</summary>

- `test_zero_total_does_not_render`
- `test_zero_total_does_not_divide_by_zero`
- `test_completed_greater_than_total_does_not_overflow_bar`
- `test_double_finish_is_safe`
- `test_finish_without_render_is_safe`
- `test_update_after_finish_is_silent`
- `test_broken_isatty_does_not_crash`

</details>

<details>
<summary><code>TestMakeProgressCallbackFactory</code> (6 tests)</summary>

- `test_no_bar_true_returns_noops`
- `test_non_tty_stream_returns_noops`
- `test_tty_stream_returns_active_callbacks`
- `test_no_bar_overrides_tty_detection`
- `test_noops_accept_correct_signature`
- `test_custom_label_propagates`

</details>

### `tests/cli/test_sarif_args.py` (23 tests)

<details>
<summary><code>ParsingTests</code> (7 tests)</summary>

- `test_default_is_none`
- `test_explicit_value_with_equals`
- `test_explicit_value_with_space`
- `test_empty_string_value_parses`
- `test_env_var_provides_default`
- `test_cli_overrides_env_var`
- `test_empty_env_var_treated_as_unset`

</details>

<details>
<summary><code>SubparserDefaultTests</code> (2 tests)</summary>

- `test_subparser_default_is_suppress`
- `test_top_level_value_survives_subparser`

</details>

<details>
<summary><code>HelperTests</code> (4 tests)</summary>

- `test_returns_none_when_attr_missing`
- `test_returns_none_when_value_is_none`
- `test_returns_none_when_value_is_empty_string`
- `test_returns_value_when_set`

</details>

<details>
<summary><code>ValidationTests</code> (10 tests)</summary>

- `test_no_warning_when_unset`
- `test_no_warning_when_unset_and_format_is_sarif`
- `test_no_warning_when_set_and_format_is_sarif`
- `test_warning_when_set_and_format_is_json`
- `test_warning_when_set_and_format_is_human`
- `test_warning_when_set_and_format_is_none`
- `test_warning_says_value_will_be_ignored`
- `test_empty_string_does_not_trigger_warning`
- `test_uses_sys_stderr_by_default`
- `test_no_hard_errors_raised`

</details>

### `tests/cli/test_scan_loose_file.py` (15 tests)

<details>
<summary><code>PathPreservationTests</code> (4 tests)</summary>

- `test_real_path_in_artifact_identity`
- `test_real_path_in_finding_internal_path`
- `test_path_in_pth_findings`
- `test_path_with_directory_components_preserved`

</details>

<details>
<summary><code>FileKindOverrideTests</code> (4 tests)</summary>

- `test_arbitrary_filename_treated_as_setup_py`
- `test_same_content_different_kind_yields_different_severity`
- `test_context_carries_forced_kind`
- `test_triage_reason_indicates_single_file_mode`

</details>

<details>
<summary><code>ApiBoundaryTests</code> (3 tests)</summary>

- `test_skip_kind_raises`
- `test_nonexistent_path_returns_diagnostic`
- `test_directory_path_returns_diagnostic`

</details>

<details>
<summary><code>PipelineEquivalenceTests</code> (2 tests)</summary>

- `test_same_signals_via_both_paths`
- `test_statistics_consistent_with_scan_bytes`

</details>

<details>
<summary><code>ArtifactKindTests</code> (2 tests)</summary>

- `test_loose_file_artifact_kind`
- `test_pth_loose_file_artifact_kind`

</details>

### `tests/cli/test_scan_single.py` (28 tests)

<details>
<summary><code>FileKindAutodetectTests</code> (7 tests)</summary>

- `test_pth_extension_is_pth`
- `test_setup_py_is_setup_py`
- `test_init_py_is_init_py`
- `test_sitecustomize_is_sitecustomize`
- `test_usercustomize_is_usercustomize`
- `test_arbitrary_py_defaults_to_setup_py`
- `test_no_extension_defaults_to_setup_py`

</details>

<details>
<summary><code>FileKindOverrideTests</code> (4 tests)</summary>

- `test_explicit_setup_py_override`
- `test_explicit_init_py_override`
- `test_every_choice_has_a_mapping`
- `test_no_choice_maps_to_skip`

</details>

<details>
<summary><code>DispatchSingleTests</code> (8 tests)</summary>

- `test_nonexistent_file_returns_diag`
- `test_directory_path_returns_diag`
- `test_arbitrary_py_file_gets_setup_py_treatment`
- `test_finding_context_carries_real_path`
- `test_artifact_identity_is_real_path`
- `test_pth_content_is_analyzed_as_pth`
- `test_as_override_changes_severity`
- `test_unparseable_content_does_not_crash`

</details>

<details>
<summary><code>CliSingleFlagTests</code> (9 tests)</summary>

- `test_single_flag_accepted`
- `test_single_flag_reports_real_path_in_artifact`
- `test_single_flag_reports_real_path_in_findings`
- `test_single_flag_finds_density_signal_in_garbage`
- `test_no_args_errors_clearly`
- `test_target_and_single_together_errors`
- `test_as_without_single_errors`
- `test_single_with_as_init_py`
- `test_single_with_nonexistent_file_returns_diagnostic`

</details>

### `tests/cli/test_subcommand_diag.py` (4 tests)

<details>
<summary><code>EmptyResultWithDiagTests</code> (2 tests)</summary>

- `test_no_initial_diags_default_unchanged`
- `test_initial_diags_prepended`

</details>

<details>
<summary><code>DispatchSingleErrorPathTests</code> (2 tests)</summary>

- `test_missing_path_includes_initial_diagnostics`
- `test_missing_path_default_no_diagnostics`

</details>

### `tests/cli/test_workers.py` (24 tests)

<details>
<summary><code>ParseWorkersTests</code> (9 tests)</summary>

- `test_serial`
- `test_auto_returns_at_least_one`
- `test_positive_int`
- `test_one_is_valid`
- `test_zero_raises`
- `test_negative_raises`
- `test_banana_raises`
- `test_float_raises`
- `test_empty_raises`

</details>

<details>
<summary><code>AvailableCpusTests</code> (1 tests)</summary>

- `test_returns_at_least_one`

</details>

<details>
<summary><code>ResolveWorkersSerialCasesTests</code> (3 tests)</summary>

- `test_no_workers_no_force_is_silent`
- `test_workers_serial_no_warning`
- `test_workers_one_no_warning`

</details>

<details>
<summary><code>ResolveForceParallelConflictTests</code> (4 tests)</summary>

- `test_case_5_force_parallel_alone_warns`
- `test_case_1_serial_plus_force_parallel_warns`
- `test_case_2a_workers_one_plus_force_parallel_warns`
- `test_force_parallel_with_workers_two_applies`

</details>

<details>
<summary><code>ResolveAutoTests</code> (2 tests)</summary>

- `test_auto_single_cpu_emits_note`
- `test_auto_multi_cpu_no_note`

</details>

<details>
<summary><code>ResolveThrashingTests</code> (5 tests)</summary>

- `test_at_2x_no_warning_boundary_inclusive_for_user`
- `test_above_2x_warns`
- `test_above_4x_severe_warns`
- `test_above_8x_refuses`
- `test_severe_takes_precedence_over_warn`

</details>

---

## dbs

*3 files, 161 tests*

### `tests/dbs/test_pdgdb_extra.py` (24 tests)

<details>
<summary><code>TestInitializeSchemaLastModified</code> (4 tests)</summary>

- `test_writes_last_modified_on_fresh_database`
- `test_last_modified_is_parseable_iso8601`
- `test_last_modified_equals_created_at_on_fresh_database`
- `test_idempotent_call_does_not_overwrite_last_modified`

</details>

<details>
<summary><code>TestWriteScanResultLastModified</code> (1 tests)</summary>

- `test_updates_last_modified_after_write`

</details>

<details>
<summary><code>TestWriteDecodedTreeLastModified</code> (1 tests)</summary>

- `test_updates_last_modified_after_write`

</details>

<details>
<summary><code>TestWriteCveScanResult</code> (10 tests)</summary>

- `test_inserts_scan_run_with_cvescan_command`
- `test_inserts_scanned_artifact_row`
- `test_scanned_artifact_has_package_identity`
- `test_inserts_cve_scan_run_row`
- `test_cve_scan_run_linked_to_scan_run_and_artifact`
- `test_inserts_cve_findings_rows`
- `test_cve_finding_fields_stored_correctly`
- `test_zero_findings_writes_cve_scan_run_no_findings`
- `test_updates_last_modified`
- `test_producer_id_on_scan_run`

</details>

<details>
<summary><code>TestListRunsCveFindingCount</code> (5 tests)</summary>

- `test_scan_run_has_zero_cve_finding_count`
- `test_cvescan_run_has_correct_cve_finding_count`
- `test_cvescan_run_has_zero_static_finding_count`
- `test_scan_run_row_has_cve_finding_count_field`
- `test_mixed_runs_counts_are_independent`

</details>

<details>
<summary><code>TestGetDbStatusLastModified</code> (3 tests)</summary>

- `test_last_modified_populated_on_fresh_database`
- `test_last_modified_updates_after_write`
- `test_last_modified_is_none_when_table_missing`

</details>

### `tests/dbs/test_pdgdb_read_write.py` (70 tests)

<details>
<summary><code>TestParseWheelName</code> (6 tests)</summary>

- `test_valid_wheel_returns_name_and_version`
- `test_name_normalized_to_lowercase_underscores`
- `test_hyphenated_name_normalized`
- `test_sdist_filename_returns_none_none`
- `test_bare_name_returns_none_none`
- `test_wheel_with_build_tag`

</details>

<details>
<summary><code>TestParseSdistName</code> (3 tests)</summary>

- `test_tar_gz_returns_name_and_version`
- `test_zip_returns_name_and_version`
- `test_wheel_filename_returns_none_none`

</details>

<details>
<summary><code>TestResolvePackageIdentity</code> (6 tests)</summary>

- `test_wheel_kind_uses_wheel_parser`
- `test_sdist_kind_uses_sdist_parser`
- `test_loose_file_returns_none_none`
- `test_installed_env_returns_name_when_package_not_found`
- `test_installed_env_normalizes_name`
- `test_installed_env_resolves_version_via_metadata`

</details>

<details>
<summary><code>TestWriteScanResult</code> (14 tests)</summary>

- `test_returns_int_tuple`
- `test_inserts_scan_run_row`
- `test_inserts_scanned_artifact_row`
- `test_inserts_file_identity_per_unique_file`
- `test_deduplicates_file_identity_for_same_file`
- `test_inserts_static_finding_per_finding`
- `test_static_finding_rule_id_is_null`
- `test_static_finding_producer_id_matches_argument`
- `test_internal_path_backslashes_normalized`
- `test_file_identity_path_also_normalized`
- `test_suppressed_findings_not_written`
- `test_zero_findings_writes_artifact_row`
- `test_installed_env_artifact_hashes_are_null`
- `test_static_finding_fields_correct`

</details>

<details>
<summary><code>TestWriteDecodedTree</code> (11 tests)</summary>

- `test_empty_tree_writes_no_rows`
- `test_flat_tree_inserts_one_node_per_top_level`
- `test_recursive_tree_child_has_parent_node_id`
- `test_top_level_node_has_null_parent`
- `test_child_findings_written_and_linked`
- `test_chain_stored_as_json_array`
- `test_indicators_stored_as_json_array`
- `test_pickle_warning_true_stored_as_1`
- `test_pickle_warning_false_stored_as_0`
- `test_ioc_decoded_source_not_written`
- `test_write_decoded_tree_failure_does_not_affect_scan_run`

</details>

<details>
<summary><code>TestGetDbStatus</code> (5 tests)</summary>

- `test_fresh_database_counts_are_zero`
- `test_schema_version_populated`
- `test_db_path_returned`
- `test_counts_reflect_written_records`
- `test_handles_empty_database_gracefully`

</details>

<details>
<summary><code>TestListRuns</code> (8 tests)</summary>

- `test_empty_database_returns_empty_list`
- `test_returns_one_row_per_run`
- `test_rows_are_newest_first`
- `test_finding_count_is_correct`
- `test_artifact_count_is_correct`
- `test_limit_restricts_results`
- `test_limit_none_returns_all`
- `test_offset_skips_leading_rows`

</details>

<details>
<summary><code>TestQueryByPackage</code> (6 tests)</summary>

- `test_returns_matching_artifacts`
- `test_name_matching_is_case_insensitive`
- `test_hyphenated_query_matches_underscore_stored`
- `test_version_filter_narrows_results`
- `test_no_match_returns_empty_list`
- `test_finding_count_is_correct`

</details>

<details>
<summary><code>TestQueryByArtifactSha512</code> (3 tests)</summary>

- `test_returns_matching_artifact`
- `test_matching_is_case_insensitive`
- `test_no_match_returns_empty_list`

</details>

<details>
<summary><code>TestExplainRun</code> (8 tests)</summary>

- `test_returns_none_for_unknown_run_id`
- `test_returns_run_explanation_for_known_run`
- `test_explanation_metadata_fields`
- `test_findings_sorted_by_path_line_col`
- `test_artifact_populated`
- `test_decoded_nodes_included`
- `test_decoded_node_chain_deserialized_as_tuple`
- `test_decoded_node_pickle_warning_deserialized_as_bool`

</details>

### `tests/dbs/test_pdgdb_schema.py` (67 tests)

<details>
<summary><code>TestConnect</code> (7 tests)</summary>

- `test_foreign_keys_on`
- `test_journal_mode_wal_for_file_db`
- `test_application_id_set`
- `test_busy_timeout_set`
- `test_accepts_str_path`
- `test_accepts_path_object`
- `test_application_id_distinct_from_cvedb`

</details>

<details>
<summary><code>TestInitializeSchema</code> (7 tests)</summary>

- `test_creates_all_tables`
- `test_creates_expected_indexes`
- `test_writes_schema_version`
- `test_writes_pydepgate_version`
- `test_writes_created_at`
- `test_idempotent`
- `test_does_not_overwrite_existing_schema_version`

</details>

<details>
<summary><code>TestCheckSchemaCompatibility</code> (5 tests)</summary>

- `test_passes_on_fresh_database`
- `test_raises_when_version_absent`
- `test_raises_when_version_wrong`
- `test_mismatch_actual_none_when_table_missing`
- `test_mismatch_message_mentions_migrate_command`

</details>

<details>
<summary><code>TestReadSchemaVersion</code> (3 tests)</summary>

- `test_returns_current_version_on_fresh_db`
- `test_returns_none_when_key_absent`
- `test_returns_none_when_table_missing`

</details>

<details>
<summary><code>TestApplyPendingMigrations</code> (6 tests)</summary>

- `test_returns_empty_list_when_no_migrations`
- `test_applies_synthetic_migration`
- `test_does_not_reapply_applied_migration`
- `test_raises_migration_error_on_bad_sql`
- `test_failed_migration_not_recorded`
- `test_updates_schema_version_after_applying`

</details>

<details>
<summary><code>TestListAppliedMigrations</code> (3 tests)</summary>

- `test_returns_empty_on_fresh_database`
- `test_returns_applied_entries_after_migration`
- `test_returns_empty_when_table_missing`

</details>

<details>
<summary><code>TestWriteReadMetadata</code> (8 tests)</summary>

- `test_write_and_read_single_key`
- `test_overwrite_updates_value`
- `test_read_missing_key_returns_none`
- `test_read_metadata_table_missing_returns_none`
- `test_write_metadata_dict_writes_multiple_keys`
- `test_read_all_metadata_returns_all_entries`
- `test_read_all_metadata_sorted_by_key`
- `test_read_all_metadata_table_missing_returns_empty`

</details>

<details>
<summary><code>TestDropAllTables</code> (3 tests)</summary>

- `test_removes_all_tables`
- `test_idempotent_on_empty_database`
- `test_schema_reinitializes_after_drop`

</details>

<details>
<summary><code>TestTableColumns</code> (8 tests)</summary>

- `test_scan_runs_columns`
- `test_scanned_artifacts_columns`
- `test_file_identities_columns`
- `test_static_findings_columns`
- `test_decoded_nodes_columns`
- `test_decoded_child_findings_columns`
- `test_cve_scan_runs_columns`
- `test_cve_findings_columns`

</details>

<details>
<summary><code>TestForeignKeys</code> (5 tests)</summary>

- `test_static_finding_bad_scan_run_id_raises`
- `test_cascade_delete_scan_run_removes_static_findings`
- `test_cascade_delete_scan_run_removes_scanned_artifacts`
- `test_cascade_delete_decoded_node_removes_child_findings`
- `test_delete_file_identity_nulls_finding_reference`

</details>

<details>
<summary><code>TestDataRoundTrips</code> (12 tests)</summary>

- `test_scan_run_round_trip`
- `test_scanned_artifact_round_trip`
- `test_scanned_artifact_nullable_fields_store_null`
- `test_file_identity_round_trip`
- `test_static_finding_round_trip_all_fields`
- `test_static_finding_round_trip_nullable_fields_null`
- `test_decoded_node_flat_round_trip`
- `test_decoded_node_child_links_to_parent`
- `test_decoded_child_finding_round_trip`
- `test_cve_scan_run_round_trip`
- `test_cve_finding_round_trip_all_fields`
- `test_cve_finding_nullable_fields_store_null`

</details>

---

## engines

*4 files, 63 tests*

### `tests/engines/test_deploy_the_pickle.py` (20 tests)

<details>
<summary><code>FileScanInputPickleTests</code> (3 tests)</summary>

- `test_minimal_input_pickles`
- `test_input_with_forced_kind_pickles`
- `test_input_with_large_content_pickles`

</details>

<details>
<summary><code>FileScanOutputPickleTests</code> (2 tests)</summary>

- `test_empty_output_pickles`
- `test_output_with_findings_pickles`

</details>

<details>
<summary><code>SkippedOutputPickleTests</code> (2 tests)</summary>

- `test_triaged_skip_output_pickles`
- `test_forced_skip_output_pickles`

</details>

<details>
<summary><code>PerAnalyzerPickleTests</code> (5 tests)</summary>

- `test_encoding_abuse_picklable`
- `test_dynamic_execution_picklable`
- `test_string_ops_picklable`
- `test_suspicious_stdlib_picklable`
- `test_code_density_picklable`

</details>

<details>
<summary><code>StaticEnginePickleTests</code> (5 tests)</summary>

- `test_engine_with_no_analyzers_pickles`
- `test_engine_with_all_analyzers_pickles`
- `test_engine_with_default_rules_pickles`
- `test_engine_method_is_picklable`
- `test_engine_with_initial_diagnostics_pickles`

</details>

<details>
<summary><code>PayloadPeekPickleTests</code> (3 tests)</summary>

- `test_default_config_pickles`
- `test_custom_config_pickles`
- `test_engine_with_payload_peek_pickles`

</details>

### `tests/engines/test_engine_progress.py` (8 tests)

<details>
<summary><code>TestEngineProgressCallback</code> (6 tests)</summary>

- `test_callback_invoked_once_per_file`
- `test_callback_completed_counts_increment`
- `test_callback_total_is_input_count`
- `test_callback_final_call_has_completed_equal_total`
- `test_no_callback_does_not_crash`
- `test_zero_files_no_callback_invocations`

</details>

<details>
<summary><code>TestEngineProgressRobustness</code> (2 tests)</summary>

- `test_callback_that_raises_does_not_abort_scan`
- `test_callback_with_wrong_signature_does_not_abort_scan`

</details>

### `tests/engines/test_pipeline.py` (17 tests)

<details>
<summary><code>PureFunctionShapeTests</code> (4 tests)</summary>

- `test_repeated_calls_produce_same_findings`
- `test_call_does_not_mutate_engine_analyzers_tuple`
- `test_output_is_a_filescanoutput`
- `test_output_internal_path_echoes_input`

</details>

<details>
<summary><code>WrapperEquivalenceTests</code> (2 tests)</summary>

- `test_scan_bytes_and_scan_loose_file_as_agree`
- `test_both_paths_use_scan_one_file`

</details>

<details>
<summary><code>PerFileStatisticsPopulationTests</code> (3 tests)</summary>

- `test_scan_bytes_has_no_per_file_stats`
- `test_scan_loose_file_as_has_no_per_file_stats`
- `test_aggregate_outputs_populates_per_file_stats`

</details>

<details>
<summary><code>AggregationCorrectnessTests</code> (5 tests)</summary>

- `test_files_total_includes_pre_skips_and_outputs`
- `test_files_scanned_only_counts_scanned_outputs`
- `test_files_skipped_includes_pre_skips_and_triage_skips`
- `test_signals_emitted_sums_over_outputs`
- `test_skipped_field_includes_both_pre_and_triage_skips`

</details>

<details>
<summary><code>ForcedFileKindTests</code> (3 tests)</summary>

- `test_forced_kind_treats_arbitrary_filename_as_setup_py`
- `test_no_forced_kind_lets_triage_skip`
- `test_forced_skip_is_handled_defensively`

</details>

### `tests/engines/test_static_engine.py` (18 tests)

<details>
<summary><code>StaticEngineScopeTests</code> (3 tests)</summary>

- `test_unknown_file_type_is_skipped`
- `test_skip_reason_is_populated`
- `test_file_in_tests_directory_is_skipped`

</details>

<details>
<summary><code>StaticEngineSetupPyTests</code> (3 tests)</summary>

- `test_clean_setup_py_produces_no_findings`
- `test_setup_py_with_exec_base64_produces_finding`
- `test_severity_uses_rule_when_default_applies`

</details>

<details>
<summary><code>StaticEngineInitPyTests</code> (2 tests)</summary>

- `test_top_level_init_is_analyzed`
- `test_deep_init_is_skipped`

</details>

<details>
<summary><code>StaticEnginePthTests</code> (4 tests)</summary>

- `test_clean_pth_produces_no_findings`
- `test_pth_exec_line_with_encoding_abuse_is_detected`
- `test_pth_exec_line_location_remapped_correctly`
- `test_pth_path_only_lines_produce_no_findings`

</details>

<details>
<summary><code>StaticEngineFileTests</code> (2 tests)</summary>

- `test_scan_file_on_existing_pth`
- `test_scan_file_on_nonexistent_path`

</details>

<details>
<summary><code>StaticEngineStatisticsTests</code> (3 tests)</summary>

- `test_files_scanned_counted`
- `test_signals_emitted_counted`
- `test_duration_is_recorded`

</details>

<details>
<summary><code>StaticEngineAnalyzerErrorTests</code> (1 tests)</summary>

- `test_analyzer_exception_recorded_in_diagnostics`

</details>

---

## enrichers

*16 files, 566 tests*

### `tests/enrichers/test_archive.py` (58 tests)

<details>
<summary><code>CRCTableTests</code> (3 tests)</summary>

- `test_table_has_256_entries`
- `test_table_zero_is_zero`
- `test_byte_update_matches_zlib`

</details>

<details>
<summary><code>CipherInitTests</code> (5 tests)</summary>

- `test_empty_password_keys_unchanged`
- `test_single_char_password_changes_all_three_keys`
- `test_keys_remain_uint32_after_long_password`
- `test_different_passwords_yield_different_keys`
- `test_init_returns_independent_lists`

</details>

<details>
<summary><code>CipherUpdateTests</code> (3 tests)</summary>

- `test_update_advances_state`
- `test_update_mutates_in_place_returns_none`
- `test_update_preserves_uint32_across_all_bytes`

</details>

<details>
<summary><code>StreamByteTests</code> (2 tests)</summary>

- `test_stream_byte_in_byte_range`
- `test_stream_byte_changes_with_key_state`

</details>

<details>
<summary><code>EncryptTests</code> (6 tests)</summary>

- `test_encrypt_empty_returns_empty`
- `test_encrypt_returns_same_length`
- `test_encrypt_changes_input`
- `test_encrypt_is_deterministic_given_keys`
- `test_different_passwords_yield_different_ciphertext`
- `test_encrypt_advances_keys`

</details>

<details>
<summary><code>DosTimeDateTests</code> (4 tests)</summary>

- `test_known_value`
- `test_pre_1980_clamped`
- `test_max_representable_year`
- `test_seconds_truncated_to_two_second_resolution`

</details>

<details>
<summary><code>RoundTripBasicTests</code> (8 tests)</summary>

- `test_single_text_entry`
- `test_multiple_entries_preserve_order`
- `test_empty_content_round_trips`
- `test_subdirectory_in_name`
- `test_backslash_in_name_normalized_to_forward_slash`
- `test_unicode_filename`
- `test_large_compressible_content`
- `test_incompressible_content`

</details>

<details>
<summary><code>RoundTripPasswordTests</code> (4 tests)</summary>

- `test_default_password_is_infected`
- `test_custom_password_works`
- `test_wrong_password_fails`
- `test_long_password`

</details>

<details>
<summary><code>RoundTripCompressionTests</code> (2 tests)</summary>

- `test_deflate_default_actually_compresses`
- `test_stored_compression`

</details>

<details>
<summary><code>RoundTripFilesystemTests</code> (2 tests)</summary>

- `test_creates_parent_directories`
- `test_overwrites_existing_file`

</details>

<details>
<summary><code>ErrorPathTests</code> (6 tests)</summary>

- `test_empty_entries_list_raises`
- `test_unknown_compression_raises`
- `test_empty_filename_raises`
- `test_filename_with_null_byte_raises`
- `test_non_ascii_password_raises`
- `test_failure_after_partial_validation_does_not_create_file`

</details>

<details>
<summary><code>WireFormatTests</code> (7 tests)</summary>

- `test_starts_with_lfh_signature`
- `test_contains_eocd_signature_at_end`
- `test_lfh_has_encrypted_flag_set`
- `test_lfh_has_utf8_flag_set`
- `test_compressed_size_includes_encryption_header`
- `test_uncompressed_size_in_lfh_is_correct`
- `test_lfh_crc32_matches_plaintext_crc`

</details>

<details>
<summary><code>CDHConsistencyTests</code> (3 tests)</summary>

- `test_cdh_crc_matches_lfh`
- `test_cdh_filename_matches_lfh`
- `test_cdh_compressed_size_matches_lfh`

</details>

<details>
<summary><code>ExternalUnzipTests</code> (3 tests)</summary>

- `test_unzip_extracts_correct_content`
- `test_unzip_test_command_passes`
- `test_unzip_rejects_wrong_password`

</details>

### `tests/enrichers/test_asn1.py` (110 tests)

<details>
<summary><code>TestReadTLV</code> (11 tests)</summary>

- `test_short_form_length_basic`
- `test_short_form_length_with_content`
- `test_long_form_length_one_octet`
- `test_long_form_length_two_octets`
- `test_length_overrun_clamps_to_buffer`
- `test_indefinite_length_recovers`
- `test_non_minimal_length_recorded`
- `test_truncated_buffer_raises`
- `test_empty_buffer_raises`
- `test_offset_past_end_raises`
- `test_long_form_octets_overrun_raises`

</details>

<details>
<summary><code>TestReadOID</code> (7 tests)</summary>

- `test_rsa_encryption_oid`
- `test_two_arc_minimal`
- `test_first_arc_zero`
- `test_first_arc_two`
- `test_large_arc_uses_continuation`
- `test_empty_input_records_anomaly`
- `test_truncated_oid_records_anomaly`

</details>

<details>
<summary><code>TestReadIntegerUnsigned</code> (7 tests)</summary>

- `test_zero`
- `test_small_positive`
- `test_max_byte_no_sign`
- `test_high_bit_with_sign_byte`
- `test_non_minimal_sign_byte_records_anomaly`
- `test_empty_records_anomaly`
- `test_large_modulus_size`

</details>

<details>
<summary><code>TestReadIntegerSigned</code> (5 tests)</summary>

- `test_zero`
- `test_positive`
- `test_negative_one`
- `test_negative_large`
- `test_empty_records_anomaly`

</details>

<details>
<summary><code>TestReadUtf8String</code> (3 tests)</summary>

- `test_ascii_round_trips`
- `test_multibyte_utf8`
- `test_invalid_utf8_records_anomaly`

</details>

<details>
<summary><code>TestReadPrintableString</code> (3 tests)</summary>

- `test_alphanumeric_clean`
- `test_charset_violation_recorded`
- `test_non_ascii_bytes_recorded`

</details>

<details>
<summary><code>TestReadIa5String</code> (2 tests)</summary>

- `test_ascii_clean`
- `test_high_bit_records_anomaly`

</details>

<details>
<summary><code>TestReadBmpString</code> (3 tests)</summary>

- `test_ascii_in_bmp`
- `test_unicode_in_bmp`
- `test_odd_length_records_anomaly`

</details>

<details>
<summary><code>TestReadT61String</code> (1 tests)</summary>

- `test_always_records_ambiguity_anomaly`

</details>

<details>
<summary><code>TestReadUtcTime</code> (5 tests)</summary>

- `test_modern_year`
- `test_century_pivot_below_50`
- `test_century_pivot_above_50`
- `test_malformed_records_anomaly`
- `test_invalid_month_records_anomaly`

</details>

<details>
<summary><code>TestReadGeneralizedTime</code> (3 tests)</summary>

- `test_normal_year`
- `test_year_9999_sentinel`
- `test_malformed_records_anomaly`

</details>

<details>
<summary><code>TestLooksLikeDER</code> (6 tests)</summary>

- `test_empty_is_false`
- `test_one_byte_is_false`
- `test_sequence_tag_is_true`
- `test_sequence_tag_with_garbage_is_true`
- `test_other_tag_is_false`
- `test_random_bytes_is_false`

</details>

<details>
<summary><code>TestClassifyAnomalies</code> (7 tests)</summary>

- `test_empty_input`
- `test_one_byte_input`
- `test_outer_not_sequence`
- `test_unknown_inner_shape`
- `test_truncated_inner`
- `test_extra_trailing_bytes_recorded`
- `test_classify_never_raises_on_random_garbage`

</details>

<details>
<summary><code>TestClassifySPKI</code> (3 tests)</summary>

- `test_rsa_2048_clean`
- `test_rsa_oid_appears_in_oids_seen`
- `test_unknown_algorithm_oid`

</details>

<details>
<summary><code>TestClassifyX509VanillaCert</code> (12 tests)</summary>

- `test_kind`
- `test_no_anomalies`
- `test_version`
- `test_serial`
- `test_signature_algorithm`
- `test_subject_attrs`
- `test_self_signed_issuer_matches_subject`
- `test_validity_dates`
- `test_rsa_modulus_size`
- `test_no_extensions`
- `test_no_san`
- `test_is_format_context_subclass`

</details>

<details>
<summary><code>TestClassifyX509RichSAN</code> (16 tests)</summary>

- `test_kind`
- `test_no_anomalies`
- `test_subject_cn`
- `test_serial`
- `test_extensions_count`
- `test_extension_oids`
- `test_basic_constraints_critical`
- `test_key_usage_critical`
- `test_san_not_critical`
- `test_extension_value_hex_present`
- `test_san_entries_count`
- `test_san_dns_entries`
- `test_san_uri_entry`
- `test_san_email_entry`
- `test_san_ip_entry`
- `test_san_attached_to_san_extension`

</details>

<details>
<summary><code>TestClassifyX509Suspicious</code> (12 tests)</summary>

- `test_kind`
- `test_no_anomalies`
- `test_high_entropy_cn_extracted`
- `test_large_serial`
- `test_rsa_4096`
- `test_not_before_utc_time`
- `test_not_after_generalized_time_year_9999`
- `test_san_count`
- `test_san_dns_entry`
- `test_san_other_name_entry`
- `test_critical_unrecognized_extension_present`
- `test_oids_seen_includes_custom`

</details>

<details>
<summary><code>TestFormatContextMarker</code> (4 tests)</summary>

- `test_classification_is_format_context`
- `test_format_context_is_frozen`
- `test_classification_subclass_is_frozen`
- `test_subclass_picklable`

</details>

### `tests/enrichers/test_decode_args.py` (31 tests)

<details>
<summary><code>TristateParsingTests</code> (7 tests)</summary>

- `test_default_is_off`
- `test_explicit_off`
- `test_explicit_hashes`
- `test_explicit_full`
- `test_bare_form_maps_to_hashes_and_records_deprecation`
- `test_invalid_value_exits`
- `test_space_separated_value_works`

</details>

<details>
<summary><code>HelperFunctionTests</code> (12 tests)</summary>

- `test_decode_iocs_mode_returns_off_by_default`
- `test_decode_iocs_mode_returns_set_value`
- `test_decode_iocs_mode_falls_back_on_invalid`
- `test_decode_extract_iocs_off_returns_false`
- `test_decode_extract_iocs_hashes_returns_true`
- `test_decode_extract_iocs_full_returns_true`
- `test_decode_archive_password_default`
- `test_decode_archive_password_custom`
- `test_decode_archive_password_empty_string_treated_as_default`
- `test_decode_archive_password_none_treated_as_default`
- `test_decode_archive_compression_default_deflate`
- `test_decode_archive_compression_stored_when_flag_set`

</details>

<details>
<summary><code>ValidationTests</code> (8 tests)</summary>

- `test_hashes_without_peek_hard_errors`
- `test_full_without_peek_hard_errors`
- `test_off_without_peek_passes`
- `test_bare_form_emits_deprecation_warning`
- `test_archive_password_warning_when_iocs_not_full`
- `test_archive_stored_warning_when_iocs_not_full`
- `test_full_mode_archive_flags_no_warning`
- `test_iocs_set_without_depth_warns`

</details>

<details>
<summary><code>EnvVarHandlingTests</code> (4 tests)</summary>

- `test_env_var_sets_default`
- `test_invalid_env_var_falls_back_to_default`
- `test_cli_overrides_env`
- `test_archive_password_env_var`

</details>

### `tests/enrichers/test_decode_iocs_mode.py` (3 tests)

<details>
<summary><code>DecodePayloadIocModeTests</code> (3 tests)</summary>

- `test_hash_mode_does_not_keep_decoded_source`
- `test_full_mode_keeps_decoded_source_for_python_source`
- `test_full_mode_does_not_force_source_for_non_python_terminal`

</details>

### `tests/enrichers/test_decode_location.py` (45 tests)

<details>
<summary><code>SanitizeTargetForFilenameTests</code> (11 tests)</summary>

- `test_alphanumeric_preserved`
- `test_dot_hyphen_underscore_preserved`
- `test_real_wheel_filename_preserved`
- `test_special_characters_squashed_to_underscore`
- `test_leading_dots_stripped`
- `test_leading_underscores_stripped`
- `test_leading_hyphens_stripped`
- `test_trailing_separators_stripped`
- `test_empty_input_falls_back_to_default`
- `test_all_special_input_falls_back_to_default`
- `test_unicode_squashed_to_underscores`

</details>

<details>
<summary><code>BuildDecodeFilenameTests</code> (6 tests)</summary>

- `test_basic_pattern_with_pinned_timestamp`
- `test_nofindings_status`
- `test_json_extension`
- `test_zip_extension`
- `test_default_timestamp_is_utc_now`
- `test_no_z_suffix_in_timestamp`

</details>

<details>
<summary><code>ResolveDecodeLocationTests</code> (9 tests)</summary>

- `test_explicit_decode_location_used_as_directory`
- `test_no_decode_location_defaults_to_cwd_decoded`
- `test_empty_tree_produces_nofindings_status`
- `test_nonempty_tree_produces_findings_status`
- `test_target_derived_from_artifact_identity_basename`
- `test_target_with_special_chars_sanitized`
- `test_empty_artifact_identity_falls_back_to_unknown`
- `test_json_extension_propagated`
- `test_path_components_compose_correctly`

</details>

<details>
<summary><code>OffModeTests</code> (3 tests)</summary>

- `test_writes_single_txt_when_tree_has_nodes`
- `test_skips_when_tree_empty`
- `test_no_iocs_section_in_off_mode_report`

</details>

<details>
<summary><code>HashesModeTests</code> (3 tests)</summary>

- `test_writes_report_and_sidecar_when_tree_has_nodes`
- `test_sidecar_contains_hash_records`
- `test_skips_when_tree_empty`

</details>

<details>
<summary><code>FullModeTests</code> (6 tests)</summary>

- `test_writes_archive_and_sidecar_when_tree_has_nodes`
- `test_archive_entries_have_three_files_in_subdir`
- `test_password_and_compression_forwarded`
- `test_atomic_write_targets_tmp_first`
- `test_writes_stub_archive_when_tree_empty`
- `test_inner_subdir_uses_sanitized_target_name`

</details>

<details>
<summary><code>JsonFormatTests</code> (2 tests)</summary>

- `test_json_format_writes_single_json_file_in_off_mode`
- `test_json_format_writes_single_json_file_in_full_mode_too`

</details>

<details>
<summary><code>MinSeverityFilterTests</code> (2 tests)</summary>

- `test_filter_runs_after_decode_not_before`
- `test_keep_for_context_preserves_low_parent_with_critical_child`

</details>

<details>
<summary><code>SidecarIocsPathTests</code> (3 tests)</summary>

- `test_replaces_zip_with_iocs_txt`
- `test_replaces_txt_with_iocs_txt`
- `test_handles_filename_with_multiple_dots`

</details>

### `tests/enrichers/test_decode_payloads.py` (104 tests)

<details>
<summary><code>IsPayloadBearingTests</code> (4 tests)</summary>

- `test_returns_true_when_both_keys_present`
- `test_returns_false_when_full_value_missing`
- `test_returns_false_when_decoded_missing`
- `test_returns_false_when_context_empty`

</details>

<details>
<summary><code>FormatLocationTests</code> (3 tests)</summary>

- `test_basic_format`
- `test_zero_column`
- `test_path_with_subdirs`

</details>

<details>
<summary><code>ToChildFindingTests</code> (2 tests)</summary>

- `test_basic_conversion`
- `test_severity_enum_lowered_to_string`

</details>

<details>
<summary><code>ExtractIOCsTests</code> (7 tests)</summary>

- `test_python_source_includes_decoded_source`
- `test_non_python_omits_decoded_source`
- `test_pem_terminal_omits_decoded_source`
- `test_str_full_value_hashes_consistently_with_bytes`
- `test_includes_sha512`
- `test_extract_timestamp_is_iso8601`
- `test_invalid_utf8_in_decoded_source_falls_back_to_replace`

</details>

<details>
<summary><code>DedupePayloadFindingsTests</code> (14 tests)</summary>

- `test_empty_input_returns_empty_list`
- `test_filters_non_payload_bearing`
- `test_single_finding_produces_single_group`
- `test_two_findings_same_payload_dedupe_to_one_group`
- `test_findings_at_different_lines_not_deduped`
- `test_findings_at_different_columns_not_deduped`
- `test_findings_with_different_payloads_not_deduped`
- `test_findings_at_different_paths_not_deduped`
- `test_str_and_bytes_full_value_hash_consistently`
- `test_preserves_first_appearance_order`
- `test_triggered_by_is_sorted_alphabetically`
- `test_duplicate_signal_ids_collapse_in_triggered_by`
- `test_full_value_is_none_filters_out`
- `test_three_groups_with_internal_dedup`

</details>

<details>
<summary><code>PickPrimaryFindingTests</code> (5 tests)</summary>

- `test_single_finding_returned_directly`
- `test_higher_severity_wins_over_lower`
- `test_alphabetical_tie_break_within_severity`
- `test_severity_order_critical_high_medium_low_info`
- `test_high_beats_medium`

</details>

<details>
<summary><code>SignalReprTests</code> (4 tests)</summary>

- `test_single_signal_returns_outer_signal_id`
- `test_two_signals_joined_with_plus`
- `test_three_signals_joined`
- `test_empty_triggered_by_falls_back_to_outer`

</details>

<details>
<summary><code>DecodedNodeFieldDefaultTests</code> (3 tests)</summary>

- `test_default_triggered_by_is_empty_tuple`
- `test_explicit_triggered_by_preserved`
- `test_node_is_frozen`

</details>

<details>
<summary><code>RenderTextTests</code> (14 tests)</summary>

- `test_empty_tree`
- `test_single_node_renders_signal_id`
- `test_multi_signal_node_renders_with_plus`
- `test_three_signals_render_with_plusses`
- `test_stop_reason_depth_limit_annotated`
- `test_stop_reason_non_python_annotated`
- `test_stop_reason_decode_failed_annotated`
- `test_indicators_listed`
- `test_pickle_warning_appears_when_set`
- `test_child_findings_listed`
- `test_nested_children_render_under_outer`
- `test_nested_multi_signal_child_renders_with_plus`
- `test_iocs_section_omitted_by_default`
- `test_iocs_section_included_when_requested`

</details>

<details>
<summary><code>RenderJSONTests</code> (8 tests)</summary>

- `test_empty_tree_produces_valid_json`
- `test_node_includes_triggered_by`
- `test_node_includes_outer_signal_id`
- `test_node_serializes_all_basic_fields`
- `test_ioc_data_included_when_present`
- `test_ioc_data_omitted_when_none`
- `test_recursive_children_serialize`
- `test_child_findings_serialize`

</details>

<details>
<summary><code>DecodePayloadsDriverTests</code> (11 tests)</summary>

- `test_empty_findings_produces_empty_tree`
- `test_non_payload_bearing_findings_filtered`
- `test_single_payload_finding_produces_one_node`
- `test_two_findings_same_payload_dedupe_at_top_level`
- `test_depth_limit_stops_recursion`
- `test_non_python_terminal_stops_recursion`
- `test_decode_failed_stops_recursion`
- `test_recursive_dedup_at_inner_layer`
- `test_inner_leaf_findings_collected_as_child_findings`
- `test_extract_iocs_populates_ioc_data`
- `test_extract_iocs_false_leaves_ioc_data_none`

</details>

<details>
<summary><code>RenderSourcesTests</code> (7 tests)</summary>

- `test_empty_tree_produces_stub`
- `test_tree_with_no_ioc_data_produces_stub`
- `test_tree_with_ioc_but_no_decoded_source_produces_stub`
- `test_single_python_source_node_renders`
- `test_multi_signal_node_uses_plus_in_header`
- `test_multiple_python_source_nodes_each_get_block`
- `test_recursive_children_collected`

</details>

<details>
<summary><code>RenderIocsTests</code> (8 tests)</summary>

- `test_empty_tree_produces_stub`
- `test_tree_with_no_ioc_data_produces_stub`
- `test_single_node_produces_all_hash_lines`
- `test_hash_lines_have_two_token_shape`
- `test_chain_summary_appears_when_chain_set`
- `test_extracted_timestamp_included`
- `test_multi_signal_header_uses_plus`
- `test_multiple_nodes_all_appear_dfs_order`

</details>

<details>
<summary><code>FilterTreeBySeverityTests</code> (14 tests)</summary>

- `test_none_min_severity_returns_tree_unchanged`
- `test_threshold_below_info_acts_as_no_filter`
- `test_critical_threshold_drops_high`
- `test_critical_threshold_keeps_critical`
- `test_low_threshold_keeps_everything`
- `test_keep_low_parent_when_critical_descendant`
- `test_keep_low_parent_when_high_child_finding`
- `test_strict_filter_on_child_findings`
- `test_drop_low_parent_when_only_low_descendants`
- `test_accepts_severity_enum`
- `test_accepts_severity_string_case_insensitive`
- `test_returns_new_tree_does_not_mutate_original`
- `test_target_and_max_depth_preserved`
- `test_deeply_nested_keep_for_context`

</details>

### `tests/enrichers/test_enricher_pickle.py` (12 tests)

<details>
<summary><code>EnricherInstancePickleTests</code> (4 tests)</summary>

- `test_noop_pickles`
- `test_configurable_pickles_default_args`
- `test_configurable_pickles_custom_args`
- `test_unpickled_enricher_works`

</details>

<details>
<summary><code>StaticEngineWithEnrichersPickleTests</code> (3 tests)</summary>

- `test_engine_with_no_enrichers_still_pickles`
- `test_engine_with_noop_enricher_pickles`
- `test_engine_with_multiple_enrichers_pickles`

</details>

<details>
<summary><code>BoundMethodPickleTests</code> (2 tests)</summary>

- `test_bound_method_with_enrichers_pickles`
- `test_bound_method_with_configurable_enricher_pickles`

</details>

<details>
<summary><code>OutputPickleTests</code> (3 tests)</summary>

- `test_output_round_trips_after_enrichment`
- `test_enrichment_added_context_survives_pickle`
- `test_output_with_noop_enricher_pickles`

</details>

### `tests/enrichers/test_enricher_pipeline.py` (15 tests)

<details>
<summary><code>EnrichmentIsPureTests</code> (2 tests)</summary>

- `test_repeated_calls_produce_same_findings`
- `test_engine_attributes_not_mutated_by_enrichment`

</details>

<details>
<summary><code>EnricherOrderingTests</code> (2 tests)</summary>

- `test_enricher_sees_analyzer_output`
- `test_enricher_runs_for_every_scanned_file`

</details>

<details>
<summary><code>EnricherBackwardsCompatibilityTests</code> (4 tests)</summary>

- `test_constructor_without_enrichers_kwarg_still_works`
- `test_explicit_empty_enrichers_list_is_a_noop`
- `test_no_enrichers_findings_match_empty_enrichers`
- `test_enrichers_run_count_is_zero_with_no_enrichers`

</details>

<details>
<summary><code>EnricherFailureTests</code> (3 tests)</summary>

- `test_raising_enricher_does_not_abort_scan`
- `test_raising_enricher_does_not_block_subsequent_enrichers`
- `test_enricher_run_count_reflects_configured_count_even_on_failure`

</details>

<details>
<summary><code>EnricherChainTests</code> (2 tests)</summary>

- `test_three_enrichers_chain_in_order`
- `test_each_enricher_sees_previous_enrichers_output`

</details>

<details>
<summary><code>NoOpEnricherTests</code> (2 tests)</summary>

- `test_noop_does_not_change_findings`
- `test_noop_increments_enrichers_run_counter`

</details>

### `tests/enrichers/test_enrichment_hints.py` (23 tests)

<details>
<summary><code>StashValueHelperTests</code> (5 tests)</summary>

- `test_short_str_passes_through_unchanged`
- `test_short_bytes_passes_through_unchanged`
- `test_oversize_str_is_truncated`
- `test_oversize_bytes_is_truncated`
- `test_at_cap_exactly_does_not_truncate`

</details>

<details>
<summary><code>Dens010EnrichmentHintTests</code> (4 tests)</summary>

- `test_dens010_fires_on_fixture`
- `test_dens010_carries_payload_peek_hint`
- `test_dens010_stashes_full_value`
- `test_dens010_does_not_set_truncated_for_short_input`

</details>

<details>
<summary><code>Dens011EnrichmentHintTests</code> (3 tests)</summary>

- `test_dens011_fires_on_fixture`
- `test_dens011_carries_payload_peek_hint`
- `test_dens011_stashes_full_value`

</details>

<details>
<summary><code>Enc001EnrichmentHintTests</code> (3 tests)</summary>

- `test_enc001_fires_on_fixture`
- `test_enc001_carries_payload_peek_hint`
- `test_enc001_stashes_full_value_when_literal_present`

</details>

<details>
<summary><code>NoUnexpectedHintsTests</code> (4 tests)</summary>

- `test_dynamic_execution_signals_have_no_hint`
- `test_string_ops_signals_have_no_hint`
- `test_suspicious_stdlib_signals_have_no_hint`
- `test_other_density_signals_have_no_hint`

</details>

<details>
<summary><code>SignalEnrichmentHintsPickleTests</code> (3 tests)</summary>

- `test_default_empty_hints_pickles`
- `test_populated_hints_pickle`
- `test_full_value_in_context_pickles`

</details>

<details>
<summary><code>ReporterOmitsUnderscoreKeysTests</code> (1 tests)</summary>

- `test_underscore_keys_omitted`

</details>

### `tests/enrichers/test_file_hashes.py` (8 tests)

<details>
<summary><code>HashPairTests</code> (5 tests)</summary>

- `test_known_input`
- `test_returns_lowercase_hex`
- `test_lengths_correct`
- `test_deterministic`
- `test_different_inputs_different_hashes`

</details>

<details>
<summary><code>ScanBytesPropagatesHashesTests</code> (2 tests)</summary>

- `test_scan_bytes_populates_artifact_hashes`
- `test_scan_bytes_artifact_and_file_hashes_match_for_loose`

</details>

<details>
<summary><code>ScanLooseFileAsPropagatesHashesTests</code> (1 tests)</summary>

- `test_loose_file_hashes_match_disk_content`

</details>

### `tests/enrichers/test_magic.py` (60 tests)

<details>
<summary><code>BinaryMagicPredicateTests</code> (18 tests)</summary>

- `test_zlib_low_compression`
- `test_zlib_default_compression`
- `test_zlib_best_compression`
- `test_zlib_negative_random_bytes`
- `test_gzip_positive`
- `test_gzip_wrong_method`
- `test_bzip2_positive_with_level`
- `test_bzip2_negative_no_level`
- `test_lzma_positive`
- `test_pe_positive`
- `test_pe_negative`
- `test_elf_positive`
- `test_png_positive`
- `test_zip_positive`
- `test_pickle_protocol_2`
- `test_pickle_protocol_4`
- `test_pickle_negative_unknown_proto_byte`
- `test_pickle_negative_too_short`

</details>

<details>
<summary><code>TextEncodingPredicateTests</code> (15 tests)</summary>

- `test_base64_positive_typical`
- `test_base64_url_safe`
- `test_base64_negative_too_short`
- `test_base64_negative_outside_alphabet`
- `test_base64_rejects_pure_hex`
- `test_pure_hex_positive`
- `test_pure_hex_negative_odd_length`
- `test_pure_hex_negative_too_short`
- `test_pure_hex_with_whitespace`
- `test_hex_0x_list_positive_comma`
- `test_hex_0x_list_positive_space`
- `test_hex_0x_list_positive_mixed_separators`
- `test_hex_0x_list_negative_too_few_tokens`
- `test_hex_0x_list_negative_invalid_token`
- `test_hex_0x_list_negative_no_prefix`

</details>

<details>
<summary><code>LooksLikePythonTests</code> (6 tests)</summary>

- `test_typical_python_source`
- `test_module_with_class`
- `test_negative_english_prose`
- `test_negative_json`
- `test_negative_empty`
- `test_negative_high_nonprintable_fraction`

</details>

<details>
<summary><code>DetectFormatStrTests</code> (5 tests)</summary>

- `test_str_base64`
- `test_str_pure_hex`
- `test_str_hex_0x_list`
- `test_str_python_source`
- `test_str_ascii_fallback`

</details>

<details>
<summary><code>DetectFormatBytesTests</code> (10 tests)</summary>

- `test_bytes_pickle_takes_priority`
- `test_bytes_zlib`
- `test_bytes_gzip`
- `test_bytes_pe`
- `test_bytes_elf`
- `test_bytes_png`
- `test_bytes_zip`
- `test_bytes_ascii_falls_back_to_text_encoding`
- `test_bytes_ascii_python_source`
- `test_bytes_unrecognized_terminal`

</details>

<details>
<summary><code>ScanIndicatorsTests</code> (6 tests)</summary>

- `test_finds_subprocess`
- `test_finds_multiple`
- `test_finds_in_bytes`
- `test_returns_empty_for_clean_input`
- `test_handles_non_ascii_bytes`
- `test_indicators_in_encounter_order`

</details>

### `tests/enrichers/test_new_hashes.py` (10 tests)

<details>
<summary><code>FileScanInputHashFieldsTests</code> (3 tests)</summary>

- `test_defaults_to_none`
- `test_accepts_hex_strings`
- `test_pickles_round_trip`

</details>

<details>
<summary><code>FileScanOutputHashFieldsTests</code> (2 tests)</summary>

- `test_defaults_to_none`
- `test_pickles_round_trip`

</details>

<details>
<summary><code>ScanResultHashFieldsTests</code> (2 tests)</summary>

- `test_defaults_to_none`
- `test_pickles_round_trip`

</details>

<details>
<summary><code>DecodedTreeHashFieldsTests</code> (3 tests)</summary>

- `test_defaults_to_none`
- `test_pickles_round_trip`
- `test_filter_preserves_artifact_hashes`

</details>

### `tests/enrichers/test_new_iocs.py` (18 tests)

<details>
<summary><code>ScanContextHashFieldsTests</code> (2 tests)</summary>

- `test_defaults_to_none`
- `test_pickles_round_trip`

</details>

<details>
<summary><code>DecodedNodeContainingFileHashTests</code> (2 tests)</summary>

- `test_defaults_to_none`
- `test_pickles_round_trip`

</details>

<details>
<summary><code>FilterPreservesContainingFileHashesTests</code> (1 tests)</summary>

- `test_filter_preserves_containing_file_hashes`

</details>

<details>
<summary><code>RenderIocsArtifactHeaderTests</code> (3 tests)</summary>

- `test_artifact_header_emitted_when_hashes_populated`
- `test_artifact_header_omitted_when_no_artifact_hashes`
- `test_artifact_header_emitted_on_empty_tree_when_hashes_present`

</details>

<details>
<summary><code>RenderIocsContainingFileTests</code> (3 tests)</summary>

- `test_containing_file_emitted_when_differs_from_artifact`
- `test_containing_file_omitted_when_equals_artifact`
- `test_containing_file_omitted_when_node_lacks_hash`

</details>

<details>
<summary><code>RenderSourcesArtifactHeaderTests</code> (1 tests)</summary>

- `test_artifact_header_in_sources_output`

</details>

<details>
<summary><code>DecodeJsonSchemaTests</code> (3 tests)</summary>

- `test_schema_version_emitted`
- `test_artifact_hashes_in_json`
- `test_containing_file_hashes_in_node_json`

</details>

<details>
<summary><code>ReporterSchemaBumpTests</code> (3 tests)</summary>

- `test_schema_version_is_3`
- `test_artifact_hashes_in_main_json`
- `test_artifact_hashes_null_for_installed_scan`

</details>

### `tests/enrichers/test_payload_peek.py` (23 tests)

<details>
<summary><code>ConstructorValidationTests</code> (6 tests)</summary>

- `test_default_construction_works`
- `test_min_length_below_floor_raises`
- `test_min_length_at_floor_works`
- `test_max_depth_zero_raises`
- `test_max_depth_negative_raises`
- `test_budget_below_floor_raises`

</details>

<details>
<summary><code>ThresholdFilteringTests</code> (2 tests)</summary>

- `test_below_threshold_signal_passes_through`
- `test_at_threshold_signal_attempts_enrichment`

</details>

<details>
<summary><code>HintFilteringTests</code> (2 tests)</summary>

- `test_signal_without_payload_peek_hint_passes_through`
- `test_signal_with_other_hint_passes_through`

</details>

<details>
<summary><code>DecodedBlockSingleLayerTests</code> (2 tests)</summary>

- `test_single_b64_layer_chain_recorded`
- `test_preview_hex_and_text_present`

</details>

<details>
<summary><code>Enc002EmissionTests</code> (6 tests)</summary>

- `test_depth_1_does_not_emit_enc002`
- `test_depth_2_emits_ambiguous_enc002`
- `test_depth_3_emits_medium_enc002`
- `test_exhausted_depth_emits_high_enc002`
- `test_enc002_does_not_request_further_enrichment`
- `test_enc002_carries_decoded_block`

</details>

<details>
<summary><code>PickleWarningTests</code> (1 tests)</summary>

- `test_pickle_inside_b64_sets_warning`

</details>

<details>
<summary><code>StatelessnessAndPicklabilityTests</code> (4 tests)</summary>

- `test_peek_is_stateless`
- `test_peek_pickles`
- `test_engine_with_peek_pickles`
- `test_post_enrichment_output_pickles`

</details>

### `tests/enrichers/test_pem_detection.py` (20 tests)

<details>
<summary><code>IsPemTests</code> (7 tests)</summary>

- `test_certificate_armor_positive`
- `test_other_armor_labels_positive`
- `test_unmatched_begin_end_negative`
- `test_begin_only_no_end_negative`
- `test_no_armor_negative`
- `test_base64_alphabet_only_negative`
- `test_empty_negative`

</details>

<details>
<summary><code>DetectFormatPemPriorityTests</code> (2 tests)</summary>

- `test_pem_text_routes_to_pem_not_base64`
- `test_pem_bytes_routes_to_pem_via_ascii_fallback`

</details>

<details>
<summary><code>FormatDetectionDetailsTests</code> (4 tests)</summary>

- `test_der_cert_bytes_attaches_classification`
- `test_non_der_binary_has_no_details`
- `test_coincidental_sequence_byte_unknown_der`
- `test_python_source_does_not_attach_details`

</details>

<details>
<summary><code>PemTransformTests</code> (6 tests)</summary>

- `test_pem_armored_cert_unwraps_to_der`
- `test_pem_terminal_classification_is_binary_unknown`
- `test_unwrap_result_details_is_der_classification`
- `test_base64_wrapped_pem_chain`
- `test_zlib_wrapped_pem_chain`
- `test_malformed_pem_decode_error`

</details>

<details>
<summary><code>BareDerInputTests</code> (1 tests)</summary>

- `test_bare_der_has_empty_chain_but_details_set`

</details>

### `tests/enrichers/test_unwrap.py` (26 tests)

<details>
<summary><code>SingleLayerChainTests</code> (7 tests)</summary>

- `test_pure_base64_unwraps_to_python_source`
- `test_pure_hex_unwraps_to_python_source`
- `test_hex_0x_list_unwraps_to_python_source`
- `test_zlib_unwraps_to_python_source`
- `test_gzip_unwraps_to_python_source`
- `test_bzip2_unwraps_to_python_source`
- `test_lzma_unwraps_to_python_source`

</details>

<details>
<summary><code>MultiLayerChainTests</code> (4 tests)</summary>

- `test_b64_zlib_source`
- `test_b64_gzip_source`
- `test_hex_zlib_source`
- `test_b64_zlib_b64_source`

</details>

<details>
<summary><code>DepthLimitTests</code> (3 tests)</summary>

- `test_depth_4_chain_triggers_exhausted_depth`
- `test_depth_1_completes_single_layer`
- `test_depth_1_exhausts_on_two_layer_chain`

</details>

<details>
<summary><code>BudgetLimitTests</code> (2 tests)</summary>

- `test_tiny_budget_triggers_exhaustion`
- `test_decompression_bomb_is_bounded`

</details>

<details>
<summary><code>ErrorPathTests</code> (2 tests)</summary>

- `test_malformed_base64_yields_decode_error`
- `test_truncated_zlib_yields_decode_error`

</details>

<details>
<summary><code>PickleDetectionTests</code> (2 tests)</summary>

- `test_pickle_protocol_2_detected_as_terminal`
- `test_pickle_through_b64_layer`

</details>

<details>
<summary><code>UnwrapResultPickleTests</code> (3 tests)</summary>

- `test_simple_result_pickles`
- `test_exhausted_result_pickles`
- `test_layer_pickles`

</details>

<details>
<summary><code>UnwrapValidationTests</code> (3 tests)</summary>

- `test_max_depth_zero_raises`
- `test_negative_max_depth_raises`
- `test_tiny_budget_raises`

</details>

---

## events

*6 files, 80 tests*

### `tests/events/test_emitter.py` (12 tests)

<details>
<summary><code>TestEventEmitterBasics</code> (6 tests)</summary>

- `test_emitter_returns_event_without_sinks`
- `test_emitter_defaults_correlation_to_run_id`
- `test_emitter_writes_to_memory_sink`
- `test_emitter_writes_to_jsonl_sink`
- `test_emitter_uses_optional_envelope_fields`
- `test_emitter_detaches_payload_through_envelope`

</details>

<details>
<summary><code>TestEventEmitterValidation</code> (6 tests)</summary>

- `test_emitter_rejects_empty_producer`
- `test_emitter_rejects_empty_run_id`
- `test_emitter_rejects_bad_sink`
- `test_emit_surfaces_envelope_validation_errors`
- `test_emit_reports_sink_failure`
- `test_configured_sinks_are_detached_from_source_sequence`

</details>

### `tests/events/test_envelope.py` (12 tests)

<details>
<summary><code>TestEventEnvelopeBasics</code> (5 tests)</summary>

- `test_envelope_builds_required_fields`
- `test_payload_is_frozen_and_detached`
- `test_mapping_proxy_payload_is_detached`
- `test_to_dict_is_json_compatible`
- `test_to_json_is_stable`

</details>

<details>
<summary><code>TestEventEnvelopeValidation</code> (7 tests)</summary>

- `test_event_type_requires_known_prefix`
- `test_event_type_requires_non_empty_string`
- `test_producer_requires_non_empty_string`
- `test_payload_must_be_mapping`
- `test_payload_keys_must_be_json_strings`
- `test_payload_rejects_bytes`
- `test_severity_must_be_supported`

</details>

### `tests/events/test_event_adversarial.py` (13 tests)

<details>
<summary><code>EventEnvelopeAdversarialTests</code> (8 tests)</summary>

- `test_rejects_bytes_like_payloads_before_json_output`
- `test_rejects_non_finite_floats`
- `test_rejects_non_string_mapping_keys`
- `test_rejects_cycles_in_payload`
- `test_payload_digest_is_stable_across_mapping_order`
- `test_sets_are_serialized_deterministically`
- `test_event_payload_is_detached_from_caller_mutation`
- `test_event_payload_rejects_direct_mutation`

</details>

<details>
<summary><code>EventEmitterAndSinkAdversarialTests</code> (5 tests)</summary>

- `test_invalid_payload_does_not_write_partial_jsonl_line`
- `test_mutating_sink_cannot_modify_event`
- `test_runtime_sink_exception_is_wrapped_with_sink_index`
- `test_tee_runtime_child_exception_is_wrapped_with_child_index`
- `test_jsonl_output_is_one_json_object_per_line`

</details>

### `tests/events/test_freeze.py` (14 tests)

<details>
<summary><code>TestDeepFreezeMappings</code> (4 tests)</summary>

- `test_mapping_becomes_mapping_proxy`
- `test_nested_mapping_is_frozen`
- `test_source_mapping_mutation_does_not_affect_frozen_value`
- `test_mapping_proxy_input_is_detached`

</details>

<details>
<summary><code>TestDeepFreezeSequences</code> (3 tests)</summary>

- `test_list_and_tuple_become_tuples`
- `test_set_and_frozenset_become_frozensets`
- `test_source_sequence_mutation_does_not_affect_frozen_value`

</details>

<details>
<summary><code>TestDeepFreezeByteContainers</code> (2 tests)</summary>

- `test_bytearray_becomes_bytes_and_is_detached`
- `test_memoryview_becomes_bytes_and_is_detached`

</details>

<details>
<summary><code>TestDeepFreezeCycles</code> (3 tests)</summary>

- `test_list_cycle_is_rejected`
- `test_mapping_cycle_is_rejected`
- `test_indirect_cycle_is_rejected`

</details>

<details>
<summary><code>TestDeepFreezeScalars</code> (2 tests)</summary>

- `test_immutable_scalars_are_returned_unchanged`
- `test_unknown_objects_are_rejected`

</details>

### `tests/events/test_scan_granting_ticket.py` (13 tests)

<details>
<summary><code>TestMintScanGrantingTicket</code> (6 tests)</summary>

- `test_mintsgt_builds_ticket`
- `test_mintsgt_records_local_invocation_evidence`
- `test_require_cli_stack_fails_without_cli_frame`
- `test_mintsgt_rejects_bad_ttl`
- `test_mintsgt_detaches_source_mappings`
- `test_to_json_is_json_compatible`

</details>

<details>
<summary><code>TestScanGrantingTicketValidation</code> (7 tests)</summary>

- `test_ticket_requires_allowed_actions`
- `test_ticket_rejects_blank_action`
- `test_ticket_rejects_string_allowed_actions`
- `test_ticket_rejects_non_mapping_budget`
- `test_ticket_rejects_non_json_metadata`
- `test_ticket_expiry_check`
- `test_ticket_fields_are_frozen`

</details>

### `tests/events/test_sinks.py` (16 tests)

<details>
<summary><code>TestMemoryEventSink</code> (6 tests)</summary>

- `test_memory_sink_stores_events`
- `test_memory_sink_returns_tuple_not_mutable_list`
- `test_memory_sink_can_be_bounded`
- `test_memory_sink_rejects_invalid_max_events`
- `test_memory_sink_rejects_non_event`
- `test_memory_sink_clear_removes_events`

</details>

<details>
<summary><code>TestJsonlEventSink</code> (5 tests)</summary>

- `test_jsonl_sink_writes_one_event_per_line`
- `test_jsonl_sink_creates_parent_directories`
- `test_jsonl_sink_truncates_on_first_write_when_append_false`
- `test_jsonl_sink_rejects_non_event`
- `test_jsonl_sink_reports_parent_creation_failure`

</details>

<details>
<summary><code>TestTeeAndNullEventSink</code> (5 tests)</summary>

- `test_tee_sink_writes_to_all_children`
- `test_tee_sink_rejects_empty_children`
- `test_tee_sink_rejects_non_sink_child`
- `test_tee_sink_reports_child_failure`
- `test_null_sink_accepts_event`

</details>

---

## introspection

*1 files, 7 tests*

### `tests/introspection/test_installed.py` (7 tests)

<details>
<summary><code>FindPackageTests</code> (2 tests)</summary>

- `test_find_pip`
- `test_find_nonexistent_package`

</details>

<details>
<summary><code>IterInstalledPackageFilesTests</code> (3 tests)</summary>

- `test_pip_has_files`
- `test_pip_has_python_source`
- `test_pydepgate_is_installed`

</details>

<details>
<summary><code>InstalledEngineIntegrationTests</code> (2 tests)</summary>

- `test_scan_installed_pip_is_clean`
- `test_scan_installed_nonexistent_package`

</details>

---

## package_tools

*2 files, 36 tests*

### `tests/package_tools/test_constants.py` (19 tests)

<details>
<summary><code>TestOsvUrls</code> (5 tests)</summary>

- `test_all_zip_url_is_https`
- `test_all_zip_url_targets_osv_storage`
- `test_all_zip_url_path_targets_pypi`
- `test_modified_id_csv_url_is_https`
- `test_modified_id_csv_url_targets_pypi`

</details>

<details>
<summary><code>TestContentTypes</code> (3 tests)</summary>

- `test_all_zip_content_types_nonempty`
- `test_modified_id_csv_content_types_nonempty`
- `test_all_zip_content_types_include_octet_stream`

</details>

<details>
<summary><code>TestSizeBounds</code> (2 tests)</summary>

- `test_modified_id_csv_min_below_max`
- `test_modified_id_csv_min_size_positive`

</details>

<details>
<summary><code>TestFilenames</code> (3 tests)</summary>

- `test_db_filename_has_db_extension`
- `test_import_zip_filename_has_zip_extension`
- `test_filenames_have_no_path_separators`

</details>

<details>
<summary><code>TestAttribution</code> (5 tests)</summary>

- `test_attribution_line_nonempty`
- `test_attribution_line_mentions_source`
- `test_attribution_line_mentions_license`
- `test_attribution_line_mentions_source_url`
- `test_license_url_is_https`

</details>

<details>
<summary><code>TestSchemaVersion</code> (1 tests)</summary>

- `test_schema_version_positive`

</details>

### `tests/package_tools/test_metadata.py` (17 tests)

<details>
<summary><code>NormalizePackageNameTests</code> (2 tests)</summary>

- `test_normalizes_case_and_separators`
- `test_collapses_separator_runs`

</details>

<details>
<summary><code>WheelFilenameTests</code> (5 tests)</summary>

- `test_parse_without_build_tag`
- `test_parse_with_build_tag`
- `test_rejects_non_wheel_filename`
- `test_rejects_wrong_component_count`
- `test_rejects_non_numeric_version_start`

</details>

<details>
<summary><code>ReadWheelMetadataTests</code> (10 tests)</summary>

- `test_dispatch_reads_wheel_metadata`
- `test_dispatch_rejects_unsupported_artifact_type`
- `test_reads_core_metadata_identity_and_package_fields`
- `test_reads_direct_url_as_declared_artifact_data`
- `test_falls_back_to_filename_when_metadata_is_absent`
- `test_falls_back_to_filename_when_metadata_is_oversized`
- `test_core_metadata_wins_but_mismatch_is_reported`
- `test_multiple_metadata_members_selects_filename_match`
- `test_multiple_metadata_members_without_match_falls_back`
- `test_unparseable_filename_can_still_use_core_metadata`

</details>

---

## package_tools/cvedb

*5 files, 162 tests*

### `tests/package_tools/cvedb/test_fetcher.py` (28 tests)

<details>
<summary><code>TestHeadCheckHappyPath</code> (3 tests)</summary>

- `test_returns_head_info_on_valid_response`
- `test_accepts_octet_stream_content_type`
- `test_strips_content_type_parameters`

</details>

<details>
<summary><code>TestHeadCheckFailures</code> (9 tests)</summary>

- `test_non_200_status_raises_head_check_error`
- `test_wrong_content_type_raises_head_check_error`
- `test_missing_content_length_raises_head_check_error`
- `test_non_integer_content_length_raises_head_check_error`
- `test_content_length_below_minimum_raises_size_limit`
- `test_content_length_above_maximum_raises_size_limit`
- `test_http_error_raises_head_check_error`
- `test_network_error_raises_download_error`
- `test_head_is_not_retried`

</details>

<details>
<summary><code>TestDownloadHappyPath</code> (6 tests)</summary>

- `test_writes_bytes_to_destination`
- `test_temp_file_removed_after_success`
- `test_sha256_matches_body`
- `test_head_info_size_validation_passes`
- `test_progress_callback_invoked`
- `test_progress_total_is_none_without_head_info`

</details>

<details>
<summary><code>TestDownloadFailures</code> (3 tests)</summary>

- `test_size_mismatch_raises_download_error`
- `test_partial_temp_removed_after_failure`
- `test_404_raises_download_error_without_retry`

</details>

<details>
<summary><code>TestDownloadRetries</code> (3 tests)</summary>

- `test_transient_error_then_success`
- `test_500_then_success`
- `test_retries_exhausted_raises`

</details>

<details>
<summary><code>TestPicklability</code> (2 tests)</summary>

- `test_head_info_round_trip`
- `test_fetch_result_round_trip`

</details>

<details>
<summary><code>TestUserAgent</code> (2 tests)</summary>

- `test_head_request_carries_user_agent`
- `test_get_request_carries_user_agent`

</details>

### `tests/package_tools/cvedb/test_importer.py` (30 tests)

<details>
<summary><code>TestRangeParser</code> (11 tests)</summary>

- `test_simple_pair`
- `test_introduced_only_open_ended`
- `test_zero_no_closer_is_all`
- `test_zero_with_fixed_not_all`
- `test_last_affected`
- `test_multiple_pairs`
- `test_dangling_after_pair`
- `test_consecutive_introduced`
- `test_fixed_without_introduced`
- `test_multiple_range_entries`
- `test_malformed_events_skipped`

</details>

<details>
<summary><code>TestParseEntryV2</code> (5 tests)</summary>

- `test_setuptools_both_versions_and_ranges`
- `test_range_only_record`
- `test_malicious_all_detected`
- `test_multi_range`
- `test_last_affected`

</details>

<details>
<summary><code>TestMergeRanges</code> (2 tests)</summary>

- `test_union_ranges`
- `test_all_packages_union`

</details>

<details>
<summary><code>TestImportWithRanges</code> (6 tests)</summary>

- `test_setuptools_writes_both`
- `test_all_versions_sentinel`
- `test_range_only_no_warning`
- `test_run_uuid_in_metadata`
- `test_default_uses_run_context`
- `test_schema_v2_recorded`

</details>

<details>
<summary><code>TestThreePhaseProgress</code> (3 tests)</summary>

- `test_all_three_phases_fire`
- `test_no_progress_works`
- `test_buggy_callback_does_not_abort`

</details>

<details>
<summary><code>TestBatchedWrites</code> (1 tests)</summary>

- `test_many_records`

</details>

<details>
<summary><code>TestPicklability</code> (2 tests)</summary>

- `test_import_result_round_trip`
- `test_parsed_record_round_trip`

</details>

### `tests/package_tools/cvedb/test_lookup.py` (25 tests)

<details>
<summary><code>NormalizePackageNameTests</code> (1 tests)</summary>

- `test_normalizes_pep503_style`

</details>

<details>
<summary><code>LookupPackageTests</code> (19 tests)</summary>

- `test_exact_version_hit_returns_vulnerability_fields`
- `test_exact_version_miss_returns_empty_result`
- `test_all_versions_sentinel_matches_any_version`
- `test_aliases_are_returned_sorted`
- `test_normalized_name_lookup_matches_database_variants`
- `test_exact_row_preferred_over_all_row_for_same_canonical`
- `test_fixed_range_row_matches_when_version_is_inside_range`
- `test_fixed_range_row_does_not_match_when_version_is_after_fix`
- `test_last_affected_range_row_matches_inclusive_upper_bound`
- `test_open_range_row_matches_from_introduced_onward`
- `test_unparseable_range_row_is_reported_but_not_matched`
- `test_git_range_row_is_reported_but_not_compared`
- `test_exact_row_preferred_over_range_row_for_same_canonical`
- `test_range_row_preferred_over_all_row_for_same_canonical`
- `test_empty_package_name_returns_warning_without_schema`
- `test_empty_version_returns_warning_without_schema`
- `test_schema_version_mismatch_propagates`
- `test_attribution_uses_db_metadata_when_present`
- `test_attribution_falls_back_to_constant`

</details>

<details>
<summary><code>LookupPackageInDbTests</code> (2 tests)</summary>

- `test_missing_db_path_raises`
- `test_file_backed_lookup`

</details>

<details>
<summary><code>PickleSafetyTests</code> (1 tests)</summary>

- `test_lookup_result_round_trip`

</details>

<details>
<summary><code>PublicCvedbShimTests</code> (2 tests)</summary>

- `test_lookup_package_shim_delegates_to_lookup_module`
- `test_lookup_package_in_db_shim_delegates_to_lookup_module`

</details>

### `tests/package_tools/cvedb/test_pepver.py` (30 tests)

<details>
<summary><code>ParseVersionTests</code> (10 tests)</summary>

- `test_parse_plain_release`
- `test_parse_epoch`
- `test_parse_pre_release_aliases`
- `test_parse_implicit_pre_release_number`
- `test_parse_post_release_aliases`
- `test_parse_implicit_post_release_number`
- `test_parse_dev_release`
- `test_parse_local_version`
- `test_parse_leading_v_and_whitespace`
- `test_reject_unparseable_versions`

</details>

<details>
<summary><code>CompareVersionTests</code> (9 tests)</summary>

- `test_release_trailing_zeroes_compare_equal`
- `test_epoch_orders_before_release`
- `test_dev_pre_final_post_ordering`
- `test_pre_release_aliases_compare_equal`
- `test_post_release_aliases_compare_equal`
- `test_local_versions_order_after_public_version`
- `test_local_version_text_sorts_before_numeric`
- `test_local_version_segments_are_compared_in_order`
- `test_unparseable_compare_returns_none`

</details>

<details>
<summary><code>RangeEvaluationTests</code> (8 tests)</summary>

- `test_version_inside_introduced_fixed_range`
- `test_introduced_is_inclusive`
- `test_fixed_is_exclusive`
- `test_last_affected_is_inclusive`
- `test_introduced_zero_means_no_lower_bound`
- `test_empty_bounds_match_parseable_version`
- `test_unparseable_candidate_returns_none`
- `test_unparseable_bound_returns_none`

</details>

<details>
<summary><code>ConveniencePredicateTests</code> (3 tests)</summary>

- `test_is_prerelease`
- `test_is_postrelease`
- `test_parsed_version_is_pickle_safe`

</details>

### `tests/package_tools/cvedb/test_schema.py` (49 tests)

<details>
<summary><code>TestConnect</code> (6 tests)</summary>

- `test_in_memory_works`
- `test_foreign_keys_enabled`
- `test_busy_timeout_set`
- `test_application_id_set_on_file`
- `test_journal_mode_wal_for_file_db`
- `test_accepts_string_or_path`

</details>

<details>
<summary><code>TestInitializeSchema</code> (5 tests)</summary>

- `test_creates_all_tables`
- `test_creates_expected_indexes`
- `test_writes_schema_version`
- `test_idempotent`
- `test_existing_version_metadata_not_overwritten`

</details>

<details>
<summary><code>TestSchemaVersion</code> (5 tests)</summary>

- `test_check_passes_after_initialize`
- `test_check_raises_when_version_absent`
- `test_check_raises_when_version_mismatch`
- `test_read_schema_version_returns_none_when_absent`
- `test_read_schema_version_raises_on_unparseable`

</details>

<details>
<summary><code>TestMetadata</code> (5 tests)</summary>

- `test_write_read_round_trip`
- `test_read_returns_none_for_missing_key`
- `test_write_overwrites_existing`
- `test_write_metadata_dict`
- `test_read_all_metadata`

</details>

<details>
<summary><code>TestForeignKeys</code> (4 tests)</summary>

- `test_alias_with_unknown_canonical_id_raises`
- `test_affected_version_with_unknown_canonical_id_raises`
- `test_delete_vuln_cascades_to_aliases`
- `test_delete_vuln_cascades_to_affected_versions`

</details>

<details>
<summary><code>TestDataIntegrity</code> (3 tests)</summary>

- `test_duplicate_alias_string_rejected`
- `test_duplicate_affected_version_triple_rejected`
- `test_different_packages_same_version_allowed`

</details>

<details>
<summary><code>TestLookupQuery</code> (2 tests)</summary>

- `test_lookup_hits`
- `test_lookup_miss_on_safe_version`

</details>

<details>
<summary><code>TestDropAllTables</code> (3 tests)</summary>

- `test_drops_all_tables`
- `test_idempotent`
- `test_can_reinitialize_after_drop`

</details>

<details>
<summary><code>TestSchemaVersionV2</code> (2 tests)</summary>

- `test_constant_is_2`
- `test_fresh_db_records_v2`

</details>

<details>
<summary><code>TestRunUuidMetadataKey</code> (2 tests)</summary>

- `test_constant_defined`
- `test_run_uuid_writes_and_reads`

</details>

<details>
<summary><code>TestAffectedRangesTable</code> (7 tests)</summary>

- `test_table_exists`
- `test_table_has_expected_columns`
- `test_optional_columns_default_to_empty_string`
- `test_primary_key_dedups_identical_ranges`
- `test_primary_key_allows_distinct_ranges`
- `test_cascade_delete_on_vulnerability`
- `test_package_index_exists`

</details>

<details>
<summary><code>TestTableNamesIncludesRanges</code> (2 tests)</summary>

- `test_affected_ranges_in_table_names`
- `test_drop_all_tables_includes_ranges`

</details>

<details>
<summary><code>TestSchemaCompatibilityWithV1Db</code> (3 tests)</summary>

- `test_v1_db_is_rejected`
- `test_v2_db_is_accepted`
- `test_no_version_metadata_is_rejected`

</details>

---

## package_tools/cvescanner

*1 files, 10 tests*

### `tests/package_tools/cvescanner/test_scanner.py` (10 tests)

<details>
<summary><code>CveScannerTests</code> (10 tests)</summary>

- `test_scan_identity_returns_exact_match_finding`
- `test_scan_identity_returns_range_match`
- `test_scan_identity_preserves_unevaluated_ranges`
- `test_scan_metadata_preserves_metadata_warnings`
- `test_scan_artifact_reads_wheel_metadata`
- `test_missing_database_is_warning_by_default`
- `test_missing_database_can_be_required`
- `test_applied_policy_result_is_preserved`
- `test_severity_unknown_for_empty_or_zero_values`
- `test_result_is_pickle_safe_when_policy_is_pickle_safe`

</details>

---

## package_tools/depresolution

*1 files, 60 tests*

### `tests/package_tools/depresolution/test_deps.py` (60 tests)

<details>
<summary><code>TestNormalization</code> (15 tests)</summary>

- `test_lowercase_only`
- `test_no_separators`
- `test_underscore_to_hyphen`
- `test_dot_to_hyphen`
- `test_mixed_separators`
- `test_collapse_consecutive_separators`
- `test_single_char`
- `test_empty_string`
- `test_dep_string_plain_name`
- `test_dep_string_with_version_specifier`
- `test_dep_string_with_marker`
- `test_dep_string_with_extras`
- `test_dep_string_with_underscores`
- `test_dep_string_leading_whitespace`
- `test_dep_string_fallback_no_name`

</details>

<details>
<summary><code>TestPythonVersionMarker</code> (12 tests)</summary>

- `test_no_python_version_constraint`
- `test_gte_matches`
- `test_gt_matches`
- `test_lte_matches`
- `test_lt_matches`
- `test_eq_matches`
- `test_neq_matches`
- `test_major_only_version`
- `test_unparseable_version_falls_back_to_include`
- `test_unknown_operator_falls_back_to_include`
- `test_compound_marker_only_first_evaluated`
- `test_quotes_optional`

</details>

<details>
<summary><code>TestRequiresDistCollection</code> (7 tests)</summary>

- `test_empty_requires_dist`
- `test_no_markers_always_included`
- `test_extras_marker_excluded`
- `test_python_version_applies`
- `test_other_markers_included_conservatively`
- `test_extras_marker_takes_precedence_over_python_version`
- `test_base_specifier_stripped`

</details>

<details>
<summary><code>TestPipReportClassification</code> (14 tests)</summary>

- `test_missing_install_key_raises`
- `test_empty_install_list`
- `test_single_root_no_deps`
- `test_single_root_with_level1_dep`
- `test_level1_and_transitive_separation`
- `test_multiple_roots`
- `test_normalization_in_classification`
- `test_yanked_preserved`
- `test_hash_extraction`
- `test_url_extraction`
- `test_missing_download_info_does_not_crash`
- `test_missing_archive_info_does_not_crash`
- `test_dep_in_multiple_roots_classified_once`
- `test_requires_dist_marker_excludes_from_level1`

</details>

<details>
<summary><code>TestCheckPipVersion</code> (6 tests)</summary>

- `test_pip_unavailable`
- `test_pip_version_output_too_short`
- `test_pip_version_unparseable`
- `test_pip_version_below_minimum`
- `test_pip_version_at_minimum`
- `test_pip_version_above_minimum`

</details>

<details>
<summary><code>TestPipResolutionReport</code> (6 tests)</summary>

- `test_successful_resolution_writes_audit_artifact`
- `test_pip_failure_cleans_up_temp_file`
- `test_timeout_cleans_up_temp_file`
- `test_json_parse_failure_cleans_up_temp_file`
- `test_stderr_warning_does_not_fail`
- `test_pip_args_include_dry_run_and_only_binary`

</details>

---

## parsers

*4 files, 61 tests*

### `tests/parsers/test_pth_parser.py` (19 tests)

<details>
<summary><code>ParserSafetyTests</code> (3 tests)</summary>

- `test_does_not_execute_import`
- `test_does_not_touch_filesystem`
- `test_handles_arbitrary_bytes_without_raising`

</details>

<details>
<summary><code>ClassificationTests</code> (9 tests)</summary>

- `test_blank_line`
- `test_comment_line`
- `test_indented_comment_is_comment`
- `test_import_with_space_is_exec`
- `test_import_with_tab_is_exec`
- `test_leading_whitespace_before_import_is_path`
- `test_from_import_is_path_not_exec`
- `test_simple_path`
- `test_line_numbers_are_one_indexed`

</details>

<details>
<summary><code>LineEndingTests</code> (3 tests)</summary>

- `test_unix_line_endings`
- `test_windows_line_endings`
- `test_mixed_line_endings`

</details>

<details>
<summary><code>EncodingTests</code> (2 tests)</summary>

- `test_utf8_success`
- `test_utf8_failure_falls_back_to_latin1`

</details>

<details>
<summary><code>ManifestTests</code> (2 tests)</summary>

- `test_all_fixtures_present`
- `test_fixtures_match_manifest`

</details>

### `tests/parsers/test_pysource_parser.py` (31 tests)

<details>
<summary><code>ParserSafetyTests</code> (9 tests)</summary>

- `test_does_not_execute_import`
- `test_does_not_execute_module_level_code`
- `test_handles_random_bytes`
- `test_handles_adversarial_binary_corpus`
- `test_tokenizer_systemerror_falls_back_to_manual_comment_scan`
- `test_detect_encoding_systemerror_is_nonfatal`
- `test_ast_parse_systemerror_is_reported_as_syntax_error`
- `test_handles_null_bytes`
- `test_handles_empty_source`

</details>

<details>
<summary><code>ParseStatusTests</code> (3 tests)</summary>

- `test_valid_source_is_ok`
- `test_syntax_error_is_reported`
- `test_syntax_error_still_returns_partial_comments`

</details>

<details>
<summary><code>CommentExtractionTests</code> (4 tests)</summary>

- `test_simple_comment`
- `test_multiple_comments`
- `test_inline_comment_column`
- `test_no_comments_in_clean_code`

</details>

<details>
<summary><code>ShebangTests</code> (3 tests)</summary>

- `test_shebang_detected_on_line_one`
- `test_shebang_not_detected_on_line_two`
- `test_regular_comment_not_shebang`

</details>

<details>
<summary><code>EncodingDeclarationTests</code> (6 tests)</summary>

- `test_encoding_declaration_on_line_one`
- `test_encoding_declaration_on_line_two`
- `test_encoding_declaration_equals_form`
- `test_encoding_declaration_not_detected_after_line_two`
- `test_suspicious_encoding_still_extracted`
- `test_invalid_encoding_falls_back_to_manual_scan`

</details>

<details>
<summary><code>DocstringVsCommentTests</code> (2 tests)</summary>

- `test_module_docstring_is_not_a_comment`
- `test_triple_quoted_string_is_not_a_comment`

</details>

<details>
<summary><code>SizeAndLineCountTests</code> (4 tests)</summary>

- `test_size_matches_input`
- `test_line_count_trailing_newline`
- `test_line_count_no_trailing_newline`
- `test_line_count_empty_source`

</details>

### `tests/parsers/test_sdist.py` (4 tests)

<details>
<summary><code>SdistEnumerationTests</code> (3 tests)</summary>

- `test_iter_simple_sdist`
- `test_unsafe_path_is_skipped`
- `test_is_sdist_on_tarball`

</details>

<details>
<summary><code>SdistEngineIntegrationTests</code> (1 tests)</summary>

- `test_scan_sdist_with_malicious_setup`

</details>

### `tests/parsers/test_wheel.py` (7 tests)

<details>
<summary><code>WheelEnumerationTests</code> (6 tests)</summary>

- `test_iter_simple_wheel`
- `test_unsafe_path_is_skipped`
- `test_absolute_path_is_skipped`
- `test_empty_wheel_yields_nothing`
- `test_is_wheel_on_valid_wheel`
- `test_is_wheel_on_non_wheel`

</details>

<details>
<summary><code>WheelEngineIntegrationTests</code> (1 tests)</summary>

- `test_scan_wheel_with_malicious_pth`

</details>

---

## pdgplatform

*1 files, 25 tests*

### `tests/pdgplatform/test_paths.py` (25 tests)

<details>
<summary><code>TestXdgCacheHome</code> (8 tests)</summary>

- `test_xdg_cache_home_env_var_wins`
- `test_xdg_cache_home_env_var_wins_on_macos`
- `test_xdg_cache_home_tilde_expanded`
- `test_linux_fallback`
- `test_macos_fallback`
- `test_windows_with_localappdata`
- `test_windows_without_localappdata`
- `test_bsd_uses_posix_default`

</details>

<details>
<summary><code>TestXdgConfigHome</code> (5 tests)</summary>

- `test_xdg_config_home_env_var_wins`
- `test_linux_fallback`
- `test_macos_fallback`
- `test_windows_with_appdata`
- `test_windows_without_appdata`

</details>

<details>
<summary><code>TestXdgDataHome</code> (4 tests)</summary>

- `test_xdg_data_home_env_var_wins`
- `test_linux_fallback`
- `test_macos_fallback`
- `test_windows_with_localappdata`

</details>

<details>
<summary><code>TestPydepgateDirs</code> (4 tests)</summary>

- `test_pydepgate_cache_dir_is_namespaced`
- `test_pydepgate_config_dir_is_namespaced`
- `test_pydepgate_data_dir_is_namespaced`
- `test_pydepgate_cache_dir_does_not_create`

</details>

<details>
<summary><code>TestEnsureDirectory</code> (4 tests)</summary>

- `test_creates_directory`
- `test_creates_parent_directories`
- `test_idempotent_on_existing_directory`
- `test_raises_when_path_is_a_file`

</details>

---

## reporters/sarif

*8 files, 300 tests*

### `tests/reporters/sarif/test_decoded_results.py` (83 tests)

<details>
<summary><code>TestEmptyNode</code> (2 tests)</summary>

- `test_no_child_findings_no_children_returns_empty`
- `test_no_child_findings_with_empty_children_returns_empty`

</details>

<details>
<summary><code>TestSingleLayerChain</code> (4 tests)</summary>

- `test_one_result_emitted`
- `test_result_rule_id_is_child_finding_signal_id`
- `test_result_rule_index_from_indices_map`
- `test_message_text_from_child_finding_description`

</details>

<details>
<summary><code>TestMultipleChildFindings</code> (2 tests)</summary>

- `test_two_child_findings_produce_two_results`
- `test_results_preserve_child_finding_order`

</details>

<details>
<summary><code>TestRuleIdMissingFromIndices</code> (1 tests)</summary>

- `test_key_error_on_unknown_signal_id`

</details>

<details>
<summary><code>TestSeverityMapping</code> (6 tests)</summary>

- `test_critical_to_error`
- `test_high_to_error`
- `test_medium_to_warning`
- `test_low_to_note`
- `test_info_to_note`
- `test_unknown_severity_string_raises_value_error`

</details>

<details>
<summary><code>TestPrimaryLocation</code> (6 tests)</summary>

- `test_uri_uses_pydepgate_decoded_scheme`
- `test_uri_includes_parent_path`
- `test_uri_includes_layer_line_column_query`
- `test_layer_count_in_uri_matches_chain_length`
- `test_inner_finding_uri_has_no_uri_base_id`
- `test_negative_column_omitted_from_uri`

</details>

<details>
<summary><code>TestRegion</code> (5 tests)</summary>

- `test_start_line_from_child_finding`
- `test_start_column_converted_to_1_indexed`
- `test_zero_column_becomes_column_1`
- `test_zero_line_falls_back_to_line_1`
- `test_negative_column_omitted_from_region`

</details>

<details>
<summary><code>TestProperties</code> (9 tests)</summary>

- `test_security_severity_present`
- `test_security_severity_matches_severity`
- `test_security_severity_is_string`
- `test_analyzer_derived_from_signal_id_prefix`
- `test_via_decode_chain_is_chain_layers_list`
- `test_outer_signal_id_for_top_level_node_is_own_id`
- `test_decode_depth_matches_node_depth`
- `test_confidence_property_omitted`
- `test_scope_property_omitted`

</details>

<details>
<summary><code>TestNestedChildren</code> (6 tests)</summary>

- `test_nested_walk_produces_one_result_per_leaf_child_finding`
- `test_nested_result_rule_id_is_innermost_signal_id`
- `test_nested_outer_signal_id_property_is_root`
- `test_nested_via_decode_chain_includes_all_layers`
- `test_nested_decode_depth_is_inner_node_depth`
- `test_nested_code_flow_walks_all_ancestors`

</details>

<details>
<summary><code>TestCodeFlowShape</code> (8 tests)</summary>

- `test_one_code_flow_per_result`
- `test_one_thread_flow_per_code_flow`
- `test_single_layer_chain_has_three_steps`
- `test_two_layer_chain_has_four_steps`
- `test_three_layer_chain_has_five_steps`
- `test_empty_chain_has_two_steps`
- `test_execution_order_is_monotonic_from_zero`
- `test_nesting_level_increments_per_layer`

</details>

<details>
<summary><code>TestCodeFlowStepShapes</code> (9 tests)</summary>

- `test_outer_step_uses_real_artifact_path`
- `test_outer_step_message_includes_signal_id_and_length`
- `test_layer_step_uses_synthetic_uri`
- `test_layer_step_message_describes_layer_kind`
- `test_layer_step_has_no_region`
- `test_second_layer_step_uses_correct_layer_number`
- `test_inner_finding_step_uses_synthetic_uri_with_full_coords`
- `test_inner_finding_step_has_region`
- `test_inner_finding_step_message_includes_signal_id`

</details>

<details>
<summary><code>TestSrcrootHandling</code> (4 tests)</summary>

- `test_outer_step_has_uri_base_id_when_use_srcroot`
- `test_outer_step_no_uri_base_id_when_use_srcroot_false`
- `test_layer_step_no_uri_base_id_even_with_srcroot`
- `test_inner_step_no_uri_base_id_even_with_srcroot`

</details>

<details>
<summary><code>TestFingerprints</code> (9 tests)</summary>

- `test_format_24_hex_colon_1`
- `test_same_inputs_produce_same_fingerprint`
- `test_different_chain_produces_different_fingerprint`
- `test_different_signal_id_produces_different_fingerprint`
- `test_different_line_produces_different_fingerprint`
- `test_different_description_produces_different_fingerprint`
- `test_different_outer_signal_id_produces_different_fingerprint`
- `test_different_parent_path_produces_different_fingerprint`
- `test_nested_chain_fingerprint_differs_from_flat`

</details>

<details>
<summary><code>TestRequiredFields</code> (2 tests)</summary>

- `test_required_top_level_fields_present`
- `test_each_thread_flow_location_has_required_subfields`

</details>

<details>
<summary><code>TestDeterminism</code> (1 tests)</summary>

- `test_same_node_produces_identical_results`

</details>

<details>
<summary><code>TestOuterLocationParsing</code> (4 tests)</summary>

- `test_simple_path_parses`
- `test_path_with_directory_parses`
- `test_path_with_embedded_colon_survives`
- `test_malformed_location_does_not_crash`

</details>

<details>
<summary><code>TestRealisticChain</code> (5 tests)</summary>

- `test_one_result_for_innermost_finding`
- `test_severity_is_critical`
- `test_full_chain_reflected_in_properties`
- `test_root_outer_signal_id_in_properties`
- `test_code_flow_walks_full_chain`

</details>

### `tests/reporters/sarif/test_document.py` (50 tests)

<details>
<summary><code>TestTopLevelShape</code> (5 tests)</summary>

- `test_returns_dict`
- `test_has_schema`
- `test_has_version`
- `test_has_exactly_one_run`
- `test_run_has_required_subfields`

</details>

<details>
<summary><code>TestToolBlock</code> (6 tests)</summary>

- `test_driver_name`
- `test_driver_organization`
- `test_driver_information_uri`
- `test_driver_semantic_version_present_and_string`
- `test_driver_rules_present_and_non_empty`
- `test_rules_sorted_by_id`

</details>

<details>
<summary><code>TestResultsArray</code> (7 tests)</summary>

- `test_empty_when_no_findings_no_decoded_tree`
- `test_contains_phase_c_results_for_findings`
- `test_contains_phase_d_results_for_decoded_tree`
- `test_phase_c_results_come_before_phase_d_results`
- `test_findings_order_preserved`
- `test_decoded_tree_node_order_preserved`
- `test_suppressed_findings_excluded`

</details>

<details>
<summary><code>TestInvocations</code> (7 tests)</summary>

- `test_exactly_one_invocation`
- `test_execution_successful_true_on_happy_path`
- `test_no_notifications_when_no_diagnostics`
- `test_notifications_present_when_diagnostics`
- `test_each_notification_has_warning_level`
- `test_notification_text_matches_diagnostic`
- `test_diagnostic_order_preserved`

</details>

<details>
<summary><code>TestAutomationDetails</code> (6 tests)</summary>

- `test_id_format_for_wheel`
- `test_id_format_for_sdist`
- `test_id_format_for_installed_env`
- `test_id_format_for_loose_file`
- `test_scan_mode_override`
- `test_id_has_trailing_slash`

</details>

<details>
<summary><code>TestOriginalUriBaseIds</code> (4 tests)</summary>

- `test_always_emitted`
- `test_has_projectroot_key`
- `test_uri_empty_when_srcroot_none`
- `test_uri_matches_srcroot_when_provided`

</details>

<details>
<summary><code>TestSrcrootPropagation</code> (2 tests)</summary>

- `test_no_srcroot_no_uri_base_id_on_results`
- `test_with_srcroot_results_get_uri_base_id`

</details>

<details>
<summary><code>TestFallbackDocument</code> (12 tests)</summary>

- `test_returns_dict`
- `test_has_schema`
- `test_has_version`
- `test_has_exactly_one_run`
- `test_tool_driver_has_identity`
- `test_tool_driver_has_no_rules`
- `test_results_empty`
- `test_execution_successful_false`
- `test_notification_with_error_level`
- `test_notification_includes_error_message`
- `test_no_automation_details`
- `test_no_uri_base_ids`

</details>

<details>
<summary><code>TestDeterminism</code> (1 tests)</summary>

- `test_same_inputs_produce_same_document`

</details>

### `tests/reporters/sarif/test_fingerprints.py` (20 tests)

<details>
<summary><code>TestOutputFormat</code> (3 tests)</summary>

- `test_returns_24_hex_chars_plus_version_suffix`
- `test_version_suffix_is_1`
- `test_digest_is_lowercase_hex`

</details>

<details>
<summary><code>TestStability</code> (4 tests)</summary>

- `test_identical_inputs_produce_identical_outputs`
- `test_path_normalization_makes_windows_match_posix`
- `test_leading_slash_does_not_affect_fingerprint`
- `test_multiple_leading_slashes_treated_same_as_one`

</details>

<details>
<summary><code>TestDifferentiation</code> (5 tests)</summary>

- `test_different_rule_id_produces_different_fingerprint`
- `test_different_path_produces_different_fingerprint`
- `test_different_line_produces_different_fingerprint`
- `test_different_context_produces_different_fingerprint`
- `test_all_inputs_different_produces_different_fingerprint`

</details>

<details>
<summary><code>TestEdgeCases</code> (7 tests)</summary>

- `test_empty_context_works`
- `test_unicode_context_works`
- `test_zero_line_works`
- `test_very_large_line_number_works`
- `test_very_long_context_works`
- `test_context_with_pipe_character_works`
- `test_path_with_pipe_character_works`

</details>

<details>
<summary><code>TestDeterminism</code> (1 tests)</summary>

- `test_identical_call_returns_identical_result_in_same_process`

</details>

### `tests/reporters/sarif/test_render.py` (23 tests)

<details>
<summary><code>TestPackageConstants</code> (5 tests)</summary>

- `test_tool_name_is_pydepgate`
- `test_tool_organization`
- `test_tool_information_uri`
- `test_sarif_version`
- `test_sarif_schema_uri`

</details>

<details>
<summary><code>TestRenderHappyPath</code> (11 tests)</summary>

- `test_output_is_valid_json`
- `test_output_ends_with_newline`
- `test_output_has_schema`
- `test_output_has_version`
- `test_tool_driver_name_is_pydepgate`
- `test_results_array_present`
- `test_invocation_marked_successful`
- `test_automation_details_for_wheel`
- `test_original_uri_base_ids_present`
- `test_srcroot_kwarg_propagates`
- `test_scan_mode_kwarg_propagates`

</details>

<details>
<summary><code>TestRenderFallback</code> (7 tests)</summary>

- `test_fallback_emitted_on_exception`
- `test_fallback_has_execution_successful_false`
- `test_fallback_includes_error_in_notification`
- `test_fallback_writes_to_stderr`
- `test_render_does_not_raise_on_assembly_failure`
- `test_fallback_output_ends_with_newline`
- `test_value_error_also_caught`

</details>

### `tests/reporters/sarif/test_results.py` (38 tests)

<details>
<summary><code>TestBasicShape</code> (5 tests)</summary>

- `test_returns_dict`
- `test_rule_id_is_signal_id`
- `test_rule_index_from_indices_map`
- `test_message_text_from_description`
- `test_unknown_signal_id_raises_key_error`

</details>

<details>
<summary><code>TestLevelMapping</code> (5 tests)</summary>

- `test_critical_produces_error`
- `test_high_produces_error`
- `test_medium_produces_warning`
- `test_low_produces_note`
- `test_info_produces_note`

</details>

<details>
<summary><code>TestLocation</code> (6 tests)</summary>

- `test_one_location_emitted_per_result`
- `test_artifact_location_uri_from_internal_path`
- `test_use_srcroot_adds_uri_base_id`
- `test_no_srcroot_omits_uri_base_id`
- `test_synthetic_decoded_path_routes_to_decoded_uri`
- `test_synthetic_decoded_path_omits_uri_base_id`

</details>

<details>
<summary><code>TestRegion</code> (5 tests)</summary>

- `test_start_line_from_signal_location`
- `test_start_column_converted_to_1_indexed`
- `test_zero_column_converts_to_column_1`
- `test_zero_line_falls_back_to_line_1`
- `test_negative_line_falls_back_to_line_1`

</details>

<details>
<summary><code>TestFingerprints</code> (7 tests)</summary>

- `test_has_primary_location_line_hash`
- `test_fingerprint_format_is_hex_colon_version`
- `test_full_value_differentiates_fingerprints`
- `test_fallback_to_description_when_no_full_value`
- `test_bytes_full_value_handled_without_crash`
- `test_invalid_utf8_bytes_handled_without_crash`
- `test_non_string_full_value_handled_via_str`

</details>

<details>
<summary><code>TestProperties</code> (8 tests)</summary>

- `test_security_severity_present`
- `test_security_severity_matches_severity`
- `test_security_severity_is_string`
- `test_analyzer_property`
- `test_confidence_property_uses_enum_name`
- `test_scope_property_uses_enum_name`
- `test_definite_confidence_handled`
- `test_function_scope_handled`

</details>

<details>
<summary><code>TestDeterminism</code> (1 tests)</summary>

- `test_same_inputs_produce_same_output`

</details>

<details>
<summary><code>TestRequiredFields</code> (1 tests)</summary>

- `test_required_fields_present`

</details>

### `tests/reporters/sarif/test_rules.py` (43 tests)

<details>
<summary><code>TestAnalyzerLookup</code> (10 tests)</summary>

- `test_dens_prefix_resolves_to_density`
- `test_dyn_prefix_resolves_to_dynamic_execution`
- `test_enc_prefix_resolves_to_encoding_abuse`
- `test_str_prefix_resolves_to_string_ops`
- `test_stdlib_prefix_resolves_to_suspicious_stdlib`
- `test_underscore_in_signal_id_does_not_break_prefix`
- `test_unknown_prefix_returns_unknown`
- `test_no_alphabetic_prefix_returns_unknown`
- `test_every_known_signal_resolves_to_known_analyzer`
- `test_analyzer_by_prefix_covers_expected_prefixes`

</details>

<details>
<summary><code>TestMakeRuleDescriptorFields</code> (5 tests)</summary>

- `test_id_is_signal_id_verbatim`
- `test_name_format_is_analyzer_slash_signal_lower`
- `test_short_description_is_first_sentence`
- `test_short_description_handles_no_period`
- `test_full_description_is_complete_text`

</details>

<details>
<summary><code>TestHelpFields</code> (6 tests)</summary>

- `test_help_text_contains_description`
- `test_help_text_contains_why_it_matters_section`
- `test_help_text_includes_common_evasions`
- `test_help_markdown_uses_bold_section_headers`
- `test_help_markdown_uses_inline_code_for_evasions`
- `test_help_omits_evasions_section_when_absent`

</details>

<details>
<summary><code>TestSeverityAndProperties</code> (8 tests)</summary>

- `test_default_configuration_level_for_critical`
- `test_default_configuration_level_for_medium`
- `test_default_configuration_level_for_info`
- `test_security_severity_for_critical_is_above_9`
- `test_security_severity_returns_string`
- `test_properties_tags_include_base_tags`
- `test_properties_tags_include_analyzer_tag`
- `test_properties_precision_is_initial_value`

</details>

<details>
<summary><code>TestMakeRulesArray</code> (10 tests)</summary>

- `test_returns_tuple_of_list_and_dict`
- `test_one_rule_per_known_signal_id`
- `test_rules_are_sorted_by_signal_id`
- `test_indices_match_array_positions`
- `test_every_rule_has_an_index_entry`
- `test_known_signal_count_matches_audit`
- `test_dens010_descriptor_well_formed`
- `test_dyn006_precursor_descriptor_present`
- `test_every_rule_has_required_sarif_fields`
- `test_every_rule_has_valid_sarif_level`

</details>

<details>
<summary><code>TestDeterminism</code> (1 tests)</summary>

- `test_same_rules_each_call`

</details>

<details>
<summary><code>TestDefaultSeverityFromRules</code> (3 tests)</summary>

- `test_dyn001_has_no_default_rule_uses_fallback`
- `test_dyn002_has_default_rules_uses_max_severity`
- `test_fallback_severity_is_medium`

</details>

### `tests/reporters/sarif/test_severity.py` (24 tests)

<details>
<summary><code>TestSarifLevelMapping</code> (7 tests)</summary>

- `test_critical_maps_to_error`
- `test_high_maps_to_error`
- `test_medium_maps_to_warning`
- `test_low_maps_to_note`
- `test_info_maps_to_note`
- `test_all_five_severities_map_to_valid_sarif_levels`
- `test_mapping_table_covers_every_severity_member`

</details>

<details>
<summary><code>TestSecuritySeverityMapping</code> (8 tests)</summary>

- `test_critical_displays_as_critical_in_github`
- `test_high_displays_as_high_in_github`
- `test_medium_displays_as_medium_in_github`
- `test_low_displays_as_low_in_github`
- `test_info_displays_as_low_in_github_below_low`
- `test_severity_ordering_preserved_in_numerics`
- `test_returns_string_per_sarif_spec`
- `test_mapping_table_covers_every_severity_member`

</details>

<details>
<summary><code>TestMappingTableConsistency</code> (2 tests)</summary>

- `test_same_keys_in_both_tables`
- `test_both_tables_cover_every_severity_member`

</details>

<details>
<summary><code>TestSeverityRanking</code> (7 tests)</summary>

- `test_rank_increases_with_severity`
- `test_critical_has_highest_rank`
- `test_info_has_lowest_rank`
- `test_rank_table_covers_every_severity_member`
- `test_max_severity_picks_higher_rank`
- `test_max_severity_returns_critical_against_anything`
- `test_max_severity_ties_return_first_argument`

</details>

### `tests/reporters/sarif/test_uris.py` (19 tests)

<details>
<summary><code>TestRealPaths</code> (8 tests)</summary>

- `test_relative_path_passes_through_unchanged`
- `test_windows_separators_normalized_to_forward_slash`
- `test_mixed_separators_all_become_forward_slash`
- `test_single_leading_slash_stripped`
- `test_multiple_leading_slashes_stripped`
- `test_use_srcroot_adds_uriBaseId`
- `test_use_srcroot_false_omits_uriBaseId`
- `test_use_srcroot_default_is_false`

</details>

<details>
<summary><code>TestSyntheticDecodedPaths</code> (9 tests)</summary>

- `test_decoded_uri_uses_pydepgate_decoded_scheme`
- `test_decoded_uri_includes_parent_path`
- `test_decoded_uri_includes_coords_as_query`
- `test_decoded_uri_without_coords_omits_query_string`
- `test_decoded_uri_url_encodes_special_chars_in_path`
- `test_decoded_uri_no_uriBaseId`
- `test_decoded_uri_normalizes_windows_separators`
- `test_decoded_uri_strips_leading_slash`
- `test_coord_values_coerced_to_strings`

</details>

<details>
<summary><code>TestSyntheticDetectionInRealPathFunction</code> (2 tests)</summary>

- `test_decoded_marker_routes_to_decoded_scheme`
- `test_decoded_marker_short_circuits_srcroot`

</details>

---

## rules

*7 files, 117 tests*

### `tests/rules/test_context_predicate.py` (44 tests)

<details>
<summary><code>TestContextPredicateNumeric</code> (8 tests)</summary>

- `test_eq_matches_exact`
- `test_ne_matches_inequal`
- `test_gt_strictly_greater`
- `test_gte_includes_boundary`
- `test_lt_strictly_less`
- `test_lte_includes_boundary`
- `test_floats_work`
- `test_type_mismatch_returns_false`

</details>

<details>
<summary><code>TestContextPredicateString</code> (6 tests)</summary>

- `test_contains_substring`
- `test_contains_works_on_lists`
- `test_startswith`
- `test_endswith`
- `test_startswith_non_string_returns_false`
- `test_endswith_non_string_returns_false`

</details>

<details>
<summary><code>TestContextPredicateCollection</code> (4 tests)</summary>

- `test_in_list`
- `test_not_in_list`
- `test_in_with_tuple`
- `test_in_with_set`

</details>

<details>
<summary><code>TestContextPredicateUnknownOp</code> (1 tests)</summary>

- `test_unknown_op_returns_false`

</details>

<details>
<summary><code>TestValidOperatorsRegistry</code> (2 tests)</summary>

- `test_contains_all_operators`
- `test_is_immutable`

</details>

<details>
<summary><code>TestContextContainsShim</code> (6 tests)</summary>

- `test_shim_creates_eq_predicates`
- `test_shim_preserves_original_field`
- `test_no_shim_when_contains_is_none`
- `test_explicit_predicates_alone`
- `test_both_fields_merge_predicates_win`
- `test_specificity_counts_shimmed_predicates`

</details>

<details>
<summary><code>TestMatchesWithPredicates</code> (4 tests)</summary>

- `test_single_predicate_match`
- `test_predicate_below_threshold`
- `test_predicate_with_missing_context_key_does_not_match`
- `test_multiple_predicates_all_must_match`

</details>

<details>
<summary><code>TestLoaderContextPredicates</code> (7 tests)</summary>

- `test_loads_valid_gte_predicate_toml`
- `test_loads_valid_in_predicate_json`
- `test_unknown_operator_with_typo_suggestion`
- `test_multiple_operators_in_one_predicate_rejected`
- `test_empty_predicate_rejected`
- `test_non_dict_predicate_rejected`
- `test_legacy_context_contains_still_works`

</details>

<details>
<summary><code>TestDens010LengthEscalation</code> (1 tests)</summary>

- `test_dens010_severity_at_boundaries`

</details>

<details>
<summary><code>TestDens011LengthEscalation</code> (1 tests)</summary>

- `test_dens011_severity_at_boundaries`

</details>

<details>
<summary><code>TestDens050LengthEscalation</code> (1 tests)</summary>

- `test_dens050_severity_at_boundaries`

</details>

<details>
<summary><code>TestLitellmRealWorldCases</code> (3 tests)</summary>

- `test_proxy_server_payload_dens010`
- `test_proxy_server_payload_dens011`
- `test_pth_backdoor_dens010`

</details>

### `tests/rules/test_defaults.py` (16 tests)

<details>
<summary><code>MatchTests</code> (9 tests)</summary>

- `test_match_on_signal_id`
- `test_no_match_on_different_signal_id`
- `test_match_on_file_kind`
- `test_no_match_on_different_file_kind`
- `test_match_requires_all_fields`
- `test_match_on_path_glob`
- `test_no_match_on_path_glob`
- `test_match_on_context_contains`
- `test_specificity_counts`

</details>

<details>
<summary><code>EvaluatorTests</code> (3 tests)</summary>

- `test_no_rules_falls_back_to_mechanical_mapping`
- `test_set_severity_rule_applies`
- `test_suppress_rule_blocks_finding`

</details>

<details>
<summary><code>SourcePrecedenceTests</code> (3 tests)</summary>

- `test_user_rule_overrides_default`
- `test_user_suppression_records_what_default_would_have_done`
- `test_specificity_within_same_source`

</details>

<details>
<summary><code>SetDescriptionTests</code> (1 tests)</summary>

- `test_description_override`

</details>

### `tests/rules/test_density_deep.py` (22 tests)

<details>
<summary><code>LibraryPyRulesPresenceTests</code> (2 tests)</summary>

- `test_all_thirteen_library_py_rules_present`
- `test_no_duplicate_rule_ids`

</details>

<details>
<summary><code>LibraryPySeverityCalibrationTests</code> (13 tests)</summary>

- `test_dens001_is_low`
- `test_dens002_is_low`
- `test_dens010_is_medium`
- `test_dens011_is_medium`
- `test_dens020_is_info`
- `test_dens021_is_info`
- `test_dens030_is_medium`
- `test_dens031_is_medium`
- `test_dens040_is_info`
- `test_dens041_is_info`
- `test_dens042_is_low`
- `test_dens050_is_high`
- `test_dens051_is_medium`

</details>

<details>
<summary><code>LibraryPyRulePrecedenceTests</code> (3 tests)</summary>

- `test_dens010_library_py_wins_over_anywhere`
- `test_dens050_library_py_wins_over_anywhere`
- `test_dens042_library_py_wins_over_anywhere`

</details>

<details>
<summary><code>LibraryPyRuleIntegrityTests</code> (4 tests)</summary>

- `test_every_library_py_rule_has_explain_text`
- `test_no_library_py_rule_explain_contains_em_dash`
- `test_every_library_py_rule_targets_library_py_file_kind`
- `test_library_py_rules_cover_all_dens_signals`

</details>

### `tests/rules/test_engine_integration.py` (3 tests)

<details>
<summary><code>EngineRulesIntegrationTests</code> (3 tests)</summary>

- `test_default_rules_promote_setup_py_findings_to_critical`
- `test_user_suppression_rule_silences_finding`
- `test_empty_rules_list_falls_back_to_mechanical_mapping`

</details>

### `tests/rules/test_evaluator.py` (16 tests)

<details>
<summary><code>MatchTests</code> (9 tests)</summary>

- `test_match_on_signal_id`
- `test_no_match_on_different_signal_id`
- `test_match_on_file_kind`
- `test_no_match_on_different_file_kind`
- `test_match_requires_all_fields`
- `test_match_on_path_glob`
- `test_no_match_on_path_glob`
- `test_match_on_context_contains`
- `test_specificity_counts`

</details>

<details>
<summary><code>EvaluatorTests</code> (3 tests)</summary>

- `test_no_rules_falls_back_to_mechanical_mapping`
- `test_set_severity_rule_applies`
- `test_suppress_rule_blocks_finding`

</details>

<details>
<summary><code>SourcePrecedenceTests</code> (3 tests)</summary>

- `test_user_rule_overrides_default`
- `test_user_suppression_records_what_default_would_have_done`
- `test_specificity_within_same_source`

</details>

<details>
<summary><code>SetDescriptionTests</code> (1 tests)</summary>

- `test_description_override`

</details>

### `tests/rules/test_explain.py` (4 tests)

<details>
<summary><code>ExplainSignalTests</code> (2 tests)</summary>

- `test_explain_known_signal`
- `test_explain_unknown_topic`

</details>

<details>
<summary><code>ExplainRuleTests</code> (1 tests)</summary>

- `test_explain_default_rule`

</details>

<details>
<summary><code>ExplainListTests</code> (1 tests)</summary>

- `test_list_shows_signals_and_rules`

</details>

### `tests/rules/test_loader.py` (12 tests)

<details>
<summary><code>JsonFormatTests</code> (2 tests)</summary>

- `test_load_simple_json_rule`
- `test_json_without_format_declaration_warns`

</details>

<details>
<summary><code>TomlFormatTests</code> (2 tests)</summary>

- `test_load_simple_toml_rule`
- `test_load_multiple_toml_rules`

</details>

<details>
<summary><code>ValidationTests</code> (5 tests)</summary>

- `test_unknown_action_rejected`
- `test_unknown_field_with_typo_suggestion`
- `test_set_severity_without_severity_field`
- `test_invalid_file_kind_rejected`
- `test_accumulated_errors_reported`

</details>

<details>
<summary><code>FileExtensionTests</code> (1 tests)</summary>

- `test_non_gate_extension_rejected`

</details>

<details>
<summary><code>DiscoveryTests</code> (2 tests)</summary>

- `test_explicit_path_returns_immediately`
- `test_no_file_found_returns_none`

</details>

---

## scanning

*2 files, 12 tests*

### `tests/scanning/test_static_runner.py` (7 tests)

<details>
<summary><code>StaticRunnerContractTests</code> (7 tests)</summary>

- `test_rejects_ticket_without_scan_action`
- `test_rejects_ruleset_fingerprint_mismatch`
- `test_rejects_loose_file_ref_for_wheel_ticket`
- `test_rejects_archive_as_loose_file_ticket`
- `test_rejects_single_budget_on_non_loose_ticket`
- `test_rejects_incompatible_ref_kind_for_wheel_ticket`
- `test_rejects_incompatible_ref_kind_for_sdist_ticket`

</details>

### `tests/scanning/test_static_runner_adversarial.py` (5 tests)

<details>
<summary><code>StaticRunnerEventAdversarialTests</code> (5 tests)</summary>

- `test_dispatch_exception_emits_scan_failed_and_reraises_original`
- `test_happy_path_event_parent_chain_and_ticket_correlation`
- `test_non_strict_sink_failure_warns_and_scan_continues`
- `test_strict_sink_failure_surfaces_event_sink_error`
- `test_decode_failure_warns_and_emits_warning_completion_event`

</details>

---

## traffic_control

*2 files, 46 tests*

### `tests/traffic_control/test_traffic_control_deep.py` (30 tests)

<details>
<summary><code>DefaultModeUnchangedTests</code> (4 tests)</summary>

- `test_random_py_skipped_in_default_mode`
- `test_deeper_init_skipped_in_default_mode`
- `test_vendored_setup_py_skipped_in_default_mode`
- `test_default_keyword_argument_matches_no_argument`

</details>

<details>
<summary><code>DeepModeUpgradesTests</code> (5 tests)</summary>

- `test_random_py_becomes_library_in_deep_mode`
- `test_deeper_init_becomes_library_in_deep_mode`
- `test_very_deep_init_becomes_library_in_deep_mode`
- `test_vendored_setup_py_becomes_library_in_deep_mode`
- `test_deeply_nested_py_becomes_library_in_deep_mode`

</details>

<details>
<summary><code>DeepModePreservesSkipsTests</code> (10 tests)</summary>

- `test_tests_directory_still_skipped`
- `test_docs_directory_still_skipped`
- `test_pycache_directory_still_skipped`
- `test_excluded_extension_still_skipped`
- `test_compiled_python_still_skipped`
- `test_native_extension_still_skipped`
- `test_init_py_inside_metadata_dir_still_skipped`
- `test_init_py_inside_excluded_dir_still_skipped`
- `test_deeper_init_inside_excluded_dir_still_skipped`
- `test_setup_py_in_examples_directory_still_skipped`

</details>

<details>
<summary><code>DeepModePreservesInScopeKindsTests</code> (6 tests)</summary>

- `test_setup_py_at_root_still_setup_py`
- `test_top_level_init_still_init_py`
- `test_pth_file_still_pth`
- `test_sitecustomize_still_sitecustomize`
- `test_usercustomize_still_usercustomize`
- `test_entry_points_still_entry_points`

</details>

<details>
<summary><code>DeepModeDecisionPayloadTests</code> (5 tests)</summary>

- `test_library_py_reason_mentions_deep_mode`
- `test_library_py_preserves_internal_path`
- `test_library_py_records_correct_depth`
- `test_deep_init_reason_mentions_deep_mode`
- `test_vendored_setup_reason_mentions_deep_mode`

</details>

### `tests/traffic_control/test_traffic_control_triage.py` (16 tests)

<details>
<summary><code>TriageTests</code> (16 tests)</summary>

- `test_top_level_setup_py`
- `test_vendored_setup_py_is_skipped`
- `test_pth_file_in_root`
- `test_pth_file_deep`
- `test_top_level_init`
- `test_deep_init_is_skipped`
- `test_sitecustomize_at_root`
- `test_sitecustomize_deep`
- `test_entry_points_in_dist_info`
- `test_entry_points_not_in_metadata_dir`
- `test_tests_directory_excluded`
- `test_init_in_tests_directory_excluded`
- `test_random_py_file_is_skipped`
- `test_binary_extension_is_skipped`
- `test_path_with_leading_slash`
- `test_path_with_backslashes`

</details>

---

## visualizers

*2 files, 67 tests*

### `tests/visualizers/test_density_map.py` (43 tests)

<details>
<summary><code>ShortCircuitTests</code> (3 tests)</summary>

- `test_empty_findings_returns_empty_string`
- `test_color_false_returns_empty_string`
- `test_color_false_and_empty_findings_returns_empty_string`

</details>

<details>
<summary><code>RenderingShapeTests</code> (8 tests)</summary>

- `test_normal_render_returns_non_empty_string`
- `test_normal_render_produces_multiline_output`
- `test_n_rows_controls_bar_height`
- `test_top_and_bottom_borders_present`
- `test_filename_appears_in_top_border`
- `test_finding_count_appears_in_bottom_border`
- `test_finding_count_singular_for_one_finding`
- `test_long_filename_is_truncated_with_ellipsis`

</details>

<details>
<summary><code>BuildBucketsTests</code> (8 tests)</summary>

- `test_buckets_have_correct_count`
- `test_finding_lands_in_proportional_bucket`
- `test_finding_at_first_line_lands_in_first_bucket`
- `test_finding_past_total_lines_clamps_to_last_bucket`
- `test_zero_total_lines_does_not_crash`
- `test_multiple_findings_same_bucket_accumulate`
- `test_bucket_worst_severity_tracks_max`
- `test_empty_buckets_default_to_info_severity`

</details>

<details>
<summary><code>FillLevelTests</code> (5 tests)</summary>

- `test_zero_count_yields_zero_fill`
- `test_zero_max_count_yields_zero_fill`
- `test_nonzero_count_yields_at_least_one`
- `test_max_count_yields_full_fill`
- `test_log_scale_compresses_large_differences`

</details>

<details>
<summary><code>RenderBarRowsTests</code> (6 tests)</summary>

- `test_returns_n_rows_strings`
- `test_no_color_omits_ansi_codes`
- `test_color_true_includes_ansi_codes_for_filled_cells`
- `test_empty_bucket_produces_only_spaces`
- `test_bottom_row_fills_first`
- `test_severity_determines_color_per_column`

</details>

<details>
<summary><code>RenderLegendRowTests</code> (6 tests)</summary>

- `test_legend_length_matches_bucket_count_when_no_color`
- `test_empty_bucket_produces_dot`
- `test_filled_bucket_produces_severity_label`
- `test_each_severity_has_distinct_label`
- `test_color_legend_includes_ansi_codes`
- `test_mixed_buckets_produce_mixed_legend`

</details>

<details>
<summary><code>CenteredBorderTests</code> (2 tests)</summary>

- `test_label_is_centered`
- `test_long_label_does_not_overflow`

</details>

<details>
<summary><code>EndToEndTests</code> (5 tests)</summary>

- `test_severity_color_from_finding_propagates_to_output`
- `test_each_finding_severity_appears_when_distributed`
- `test_total_lines_none_falls_back_to_max_finding_line`
- `test_total_lines_zero_falls_back_to_max_finding_line`
- `test_output_ends_with_newline`

</details>

### `tests/visualizers/test_peek_render.py` (24 tests)

<details>
<summary><code>SummaryRendererTests</code> (8 tests)</summary>

- `test_basic_chain_appears_in_output`
- `test_layer_count_pluralizes`
- `test_indicators_appear_when_present`
- `test_no_indicator_line_when_empty`
- `test_pickle_warning_appears`
- `test_no_pickle_warning_when_false`
- `test_status_shown_when_not_completed`
- `test_completed_status_not_repeated`

</details>

<details>
<summary><code>VerboseRendererTests</code> (7 tests)</summary>

- `test_per_layer_breakdown_shown`
- `test_final_form_summary`
- `test_full_indicator_list`
- `test_hex_dump_present`
- `test_hex_dump_alignment_for_short_input`
- `test_pickle_warning_at_bottom_in_red`
- `test_continues_as_callout_when_exhausted`

</details>

<details>
<summary><code>ColorSchemeTests</code> (4 tests)</summary>

- `test_plain_has_no_escape_codes`
- `test_ansi_inserts_bold_for_label`
- `test_none_color_treated_as_plain`
- `test_custom_color_scheme`

</details>

<details>
<summary><code>EdgeCaseTests</code> (5 tests)</summary>

- `test_empty_chain`
- `test_missing_keys_do_not_crash`
- `test_non_mapping_returns_empty`
- `test_indent_applied_to_every_line`
- `test_malformed_hex_does_not_crash`

</details>

---
