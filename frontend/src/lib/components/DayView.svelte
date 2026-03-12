<script lang="ts">
	import chevron from '$lib/assets/up-chevron.svg';
	import { buildDayViewEvents, toggleExpandedEvent } from '$lib/features/events/day-view';
	import { filteredEvents } from '$lib/stores/events';
	import { slide } from 'svelte/transition';

	let expandedEventIds: number[] = $state([]);

	let {
		selectedDate = null,
		expandedEventId = null
	}: {
		selectedDate: string | null;
		expandedEventId: number | null;
	} = $props();

	const dayEvents = $derived(buildDayViewEvents($filteredEvents, selectedDate));

	$effect(() => {
		expandedEventIds = expandedEventId != null ? [expandedEventId] : [];
		void selectedDate;
	});

	function viewDetails(eventId: number): void {
		expandedEventIds = toggleExpandedEvent(expandedEventIds, eventId);
	}

	function isExpanded(eventId: number): boolean {
		return expandedEventIds.includes(eventId);
	}
</script>

{#if selectedDate}
	<p>Showing events for: {selectedDate}</p>
{:else}
	<p>No date selected. Go back to calendar and choose a day.</p>
{/if}

<div class="dayEvent-container">
	{#if dayEvents.length > 0}
		{#each dayEvents as event (event.id)}
			<div class="event-card w-full rounded-xl p-2 shadow-sm outline outline-black/6">
				<button
					class="event-header flex h-full w-full gap-x-2 rounded-xl bg-white hover:bg-gray-100"
					type="button"
					onclick={() => viewDetails(event.id)}
				>
					<h2 class="event-title title flex align-middle font-bold">
						{event.eventTitle}
						{#if event.food}
							<span class="food-available">🍕</span>
						{/if}
						<span class="event-location text-sm"> {event.eventLocation}</span>
						<span class="event-time text-sm">@ {event.eventStartTime}</span>
					</h2>
					<span class="toggle h-6 w-6">
						<img
							class={`transition-transform duration-300 ${isExpanded(event.id) ? '' : 'rotate-180'}`}
							src={chevron}
							alt="toggle"
						/>
					</span>
				</button>

				{#if isExpanded(event.id)}
					<div class="event-details overflow-hidden" transition:slide={{ duration: 320 }}>
						<h1 class="flex gap-x-1">
							<p class="host">{event.eventHost}</p>
							<img class="" src="" alt="" />
						</h1>
						<h2 class="flex gap-x-2">
							<p class="description">{event.eventDescription}</p>
							<img class="" src="" alt="" />
						</h2>
					</div>
				{/if}
			</div>
		{/each}
	{:else if selectedDate}
		<p class="text-sm text-gray-500">No events match this date and search query.</p>
	{/if}
</div>
