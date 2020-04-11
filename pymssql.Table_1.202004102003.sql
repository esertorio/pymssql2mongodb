USE [pymssql]
GO
/****** Object:  Table [dbo].[Table_1]    Script Date: 2020-04-10 17:10:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Table_1](
	[name] [varchar](50) NULL,
	[bithdate] [datetime] NULL,
	[favoriteNumber] [int] NULL,
	[likeOvni] [bit] NULL
) ON [PRIMARY]
GO

USE [pymssql]
GO
INSERT [dbo].[Table_1] ([name], [bithdate], [favoriteNumber], [likeOvni]) VALUES (N'pateta', CAST(N'1974-03-28T11:10:00.000' AS DateTime), 7, 1)
GO
INSERT [dbo].[Table_1] ([name], [bithdate], [favoriteNumber], [likeOvni]) VALUES (N'minie', CAST(N'1974-07-22T22:21:20.000' AS DateTime), 3, 0)
GO
INSERT [dbo].[Table_1] ([name], [bithdate], [favoriteNumber], [likeOvni]) VALUES (N'falcon', CAST(N'2002-12-14T15:16:17.000' AS DateTime), 5, 0)
GO
INSERT [dbo].[Table_1] ([name], [bithdate], [favoriteNumber], [likeOvni]) VALUES (N'barbie', CAST(N'2007-03-15T16:17:18.000' AS DateTime), 6, 1)
GO
