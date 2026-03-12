<script lang="ts">
	import { resolve } from '$app/paths';
	import { buildSidebarGroups } from '$lib/features/events/sidebar';
	import { parseEventDate } from '$lib/features/events/utils';
	import { filteredEvents } from '$lib/stores/events';
	import { toLocalIsoDate } from '$lib/utils/date';

	const sidebarGroups = $derived(buildSidebarGroups(new Date(), $filteredEvents));
</script>

<aside class="flex h-full w-full flex-col rounded-lg border border-gray-200 bg-white p-3 shadow-sm">
	<h2 class="px-1 text-sm font-semibold text-gray-900">Upcoming Events</h2>
	<div class="scrollbar-hidden mt-1 min-h-32 flex-1 overflow-y-scroll">
		{#each sidebarGroups as group (group.title)}
			<p
				class="mt-4 mb-1 px-1 text-[10px] font-semibold tracking-wider text-gray-400 uppercase first:mt-1"
			>
				{group.title}
			</p>
			{#if group.events.length > 0}
				{#each group.events as event (event.id)}
					{@const eventDateParam = toLocalIsoDate(parseEventDate(event.eventDay))}
					<form action={resolve('/day')} method="GET" class="w-full">
						<input type="hidden" name="date" value={eventDateParam} />
						<input type="hidden" name="event" value={String(event.id)} />
						<button
							type="submit"
							class="block w-full rounded-lg px-2 py-2 text-left transition-colors hover:bg-gray-50"
						>
							<div class="flex items-start justify-between gap-2">
								<span class="text-sm leading-tight font-semibold text-gray-900">
									{event.eventTitle}{#if event.food}&nbsp;🍕{/if}
								</span>
								<span class="shrink-0 text-xs font-medium text-gray-500"
									>{event.eventStartTime}</span
								>
							</div>
							<p class="mt-0.5 truncate text-xs text-gray-400">{event.eventLocation}</p>
						</button>
					</form>
				{/each}
			{:else}
				<p class="px-1 text-xs text-gray-400">No matching events.</p>
			{/if}
		{/each}
	</div>
</aside>

<style>
	.scrollbar-hidden::-webkit-scrollbar {
		display: none;
	}
	.scrollbar-hidden {
		-ms-overflow-style: none;
		scrollbar-width: none;
	}
</style>
