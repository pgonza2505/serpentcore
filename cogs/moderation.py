import disnake
from disnake.ext import commands
from disnake import Option, OptionType

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.slash_command(
        name="purge",
        description="Delete a number of messages from the current channel.",
        dm_permission=False,
        default_member_permissions=disnake.Permissions(manage_messages=True),
    )
    async def purge(
        self,
        inter: disnake.ApplicationCommandInteraction,
        amount: int = commands.Param(gt=0, le=500, description="How many messages to delete (max 500)"),
    ):
        await inter.response.defer(ephemeral=True)
        deleted = await inter.channel.purge(limit=amount)
        await inter.edit_original_message(f"🧹 Deleted **{len(deleted)}** messages.")

    
    @commands.slash_command(
        name="slowmode",
        description="Set the slowmode delay for the current channel.",
        dm_permission=False,
        default_member_permissions=disnake.Permissions(manage_channels=True)
    )
    async def slowmode(
        self,
        inter: disnake.ApplicationCommandInteraction,
        seconds: int = commands.Param(ge=0, le=21600, description="Slowmode delay in seconds (0 = off)"),
    ):
        await inter.channel.edit(slowmode_delay=seconds)
        await inter.response.send_message(
            f"🐢 Slowmode set to **{seconds} seconds**.",
            ephemeral=True
        )
    
    @commands.slash_command(
        name="say",
        description="Make the bot say something in the current channel.",
        dm_permission=False,
        default_member_permissions=disnake.Permissions(manage_messages=True)
    )
    async def say(
        self,
        inter: disnake.ApplicationCommandInteraction,
        message: str = commands.Param(description="What should the bot say?"),
    ):
        await inter.response.send_message("✅ Sent.", ephemeral=True),
        await inter.channel.send(message)

    @commands.slash_command(
        name="kick",
        description="Kick a member from the server.",
        dm_permission=False,
        default_member_permissions=disnake.Permissions(kick_members=True)
    )
    async def kick(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.Member = commands.Param(description="Who should be kicked?"),
        reason: str = commands.Param(default="No reason provided.", description="Reason for kicking."),
    ):
        await inter.response.send_message(f"👢 Kicked **{user}**.", ephemeral=True),
        await user.kick(reason=reason)
    

    @commands.slash_command(
        name="ban",
        description="Ban a member from the server.",
        dm_permission=False,
        default_member_permissions=disnake.Permissions(ban_members=True)
    )
    async def ban(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.Member = commands.Param(description="Who should be banned?"),
        reason: str = commands.Param(default="No reason provided.", description="Reason for banning."),
        delete_days: int = commands.Param(default=0, ge=0, le=7, description="Delete message history (0-7 days)."),
    ):
        await inter.response.send_message(f"🔨 Banned **{user}**.", ephemeral=True)
        await inter.guild.ban(user, reason=reason, delete_message_days=delete_days)


def setup(bot):
    bot.add_cog(Moderation(bot))