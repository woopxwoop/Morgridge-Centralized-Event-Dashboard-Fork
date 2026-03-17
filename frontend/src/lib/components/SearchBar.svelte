<script lang="ts">
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import type { EventInfo } from '$lib/mockEvents';
	import {
		buildHighlightSegments,
		getEventRecencyScore,
		getEventSearchMatches,
		parseEventDate
	} from '$lib/features/events/utils';
	import { toLocalIsoDate } from '$lib/utils/date';
	import { calendarSearchQuery } from '$lib/stores/calendar-ui';

	let { events = [] }: { events: EventInfo[] } = $props();

	let query = $state('');
	let isDropdownOpen = $state(false);
	let containerElement: HTMLDivElement | null = null;

	const results = $derived.by(() => {
		const normalizedQuery = query.trim().toLowerCase();

		if (!normalizedQuery) {
			return [];
		}

		return events
			.map((event) => ({
				event,
				matches: getEventSearchMatches(event, normalizedQuery, 'preview').slice(0, 2),
				recencyScore: getEventRecencyScore(event)
			}))
			.filter((result) => result.recencyScore > Number.NEGATIVE_INFINITY)
			.sort((left, right) => right.recencyScore - left.recencyScore)
			.map((result) => ({
				...result,
				highlightedMatches: result.matches.map((match) => ({
					...match,
					segments: buildHighlightSegments(match.value, normalizedQuery)
				}))
			}))
			.filter((result) => result.matches.length > 0)
			.slice(0, 5);
	});

	function onEnter(): void {
		const normalizedQuery = query.trim();
		calendarSearchQuery.set(normalizedQuery);
		isDropdownOpen = false;
	}

	function jumpTo(event: EventInfo): void {
		const selectedDate = toLocalIsoDate(parseEventDate(event.eventDay));
		calendarSearchQuery.set(query.trim());
		let dayHref = resolve('/day');
		dayHref += `?date=${encodeURIComponent(selectedDate)}&event=${event.id}`;
		void goto(dayHref);
		isDropdownOpen = false;
		query = '';
	}

	function onFocusInput(): void {
		if (query.trim()) {
			isDropdownOpen = true;
		}
	}

	function onInput(): void {
		calendarSearchQuery.set(query.trim());
		isDropdownOpen = Boolean(query.trim());
	}

	function onWindowMouseDown(event: MouseEvent): void {
		if (!containerElement) {
			return;
		}

		const target = event.target;
		if (target instanceof Node && !containerElement.contains(target)) {
			isDropdownOpen = false;
		}
	}

	function onKeyDown(event: KeyboardEvent): void {
		if (event.key === 'Escape') {
			isDropdownOpen = false;
			return;
		}

		if (event.key !== 'Enter') {
			return;
		}

		event.preventDefault();
		onEnter();
	}
</script>

<svelte:window onmousedown={onWindowMouseDown} />

<div class="relative w-full" bind:this={containerElement}>
	<label class="block w-full">
		<span class="sr-only">Search events</span>
		<input
			type="search"
			placeholder="Search events"
			class="w-full rounded border px-3 py-1.5 text-sm"
			bind:value={query}
			onfocus={onFocusInput}
			oninput={onInput}
			onkeydown={onKeyDown}
		/>
	</label>

	{#if isDropdownOpen && results.length > 0}
		<div
			class="absolute top-full right-0 left-0 z-20 mt-1 overflow-hidden rounded-lg border border-(--uwGrayLight) bg-(--uwWhite) shadow-sm"
		>
			{#each results as result (result.event.id)}
				<button
					type="button"
					onclick={() => jumpTo(result.event)}
					class="block w-full border-b border-(--uwGrayLight) bg-(--uwWhite) px-3 py-2 text-left text-sm text-(--uwGrayDark) transition-colors last:border-b-0 hover:bg-(--uwGrayLightest)"
				>
					<div class="flex items-start justify-between gap-2">
						<p class="font-medium">{result.event.eventTitle}</p>
						<span class="shrink-0 text-xs font-medium text-(--uwRedDark)">
							{result.event.eventDay}
						</span>
					</div>
					<p class="mt-0.5 text-xs text-(--uwGrayDark)/70">
						{#each result.highlightedMatches as match, index (match.key)}
							{match.label}:
							{#each match.segments as segment, segmentIndex (segmentIndex)}
								{#if segment.matched}
									<span class="rounded bg-(--uwGrayLight) px-0.5 font-medium text-(--uwGrayDark)"
										>{segment.text}</span
									>
								{:else}{segment.text}{/if}
							{/each}
							{#if index < result.highlightedMatches.length - 1}
								•
							{/if}
						{/each}
					</p>
				</button>
			{/each}
		</div>
	{/if}
</div>
