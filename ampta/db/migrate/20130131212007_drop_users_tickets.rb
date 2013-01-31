class DropUsersTickets < ActiveRecord::Migration
  def up
    drop_table :users_tickets
  end

  def down
    raise ActiveRecord::IrreversibleMigration
  end
end
